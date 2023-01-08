import cv2
import numpy as np

image = cv2.imread('1.jpg', 1)

height, width, channel = image.shape
image = cv2.resize(image, (int(0.5 * width), int(0.5 * height)), interpolation=cv2.INTER_CUBIC)
# cv2.imshow("original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)

gray = cv2.GaussianBlur(gray, (3, 3), 1)
ret, binary = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("binary", binary)

element = cv2.getStructuringElement(cv2.MORPH_RECT,
                                    (3, 3))  # 3 * 3 квадрат, 8-битный тип uchar, все 1 структурные элементы
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, element)
# cv2.imshow("morphology", binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("find", len(contours), "contours")


# 4. Рисуем контурную функцию
# Пользовательская функция рисования контура (для упрощения операции)
# Введите 1: winName: имя окна
# Вход 2: изображение: исходное изображение
# Вход 3: контуры: контуры
# Ввод 4: draw_on_blank: метод рисования, True рисует на белом фоне, False: рисует на исходном изображении
def drawMyContours(winName, image, contours, draw_on_blank):
    # cv2.drawContours(image, contours, index, color, line_width)
    # Входные параметры:
    # изображение: изображение холста того же размера, что и исходное изображение (также может быть исходным изображением)
    # контуры: контуры (список питонов)
    # index: индекс контура (при значении -1 нарисуйте все контуры)
    # цвет: цвет линии,
    # line_width: толщина линии
    # Вернуть контурное изображение
    if (draw_on_blank):  # нарисовать контур на белом фоне

        temp = np.ones(image.shape, dtype=np.uint8) * 255
        cv2.drawContours(temp, contours, -1, (0, 0, 0), 2)
    else:
        temp = image.copy()
        cv2.drawContours(temp, contours, -1, (0, 255, 0), 1)
    cv2.imshow(winName, temp)
    cv2.waitKey()


drawMyContours("find contours", image, contours, True)


# Пользовательская функция: используется для удаления контура указанного порядкового номера в списке
# Вход 1: контуры: исходные контуры
# Ввод 2: delete_list: список номеров контуров, которые нужно удалить
# Возвращаемое значение: контуры: отфильтрованные контуры
def delet_contours(contours, delete_list):
    delta = 0
    for i in range(len(delete_list)):
        print("i= ", i)
        print('list= ', delete_list[i])
        print('delete', contours[delete_list[i] - delta])
        del list(contours)[delete_list[i] - delta]
        delta += 1
    contours = tuple(contours)
    return contours

    # 5.Фильтры контуров
    # 5.1 Фильтрация контуров с использованием иерархии
    # hierarchy[i]: [Next，Previous，First_Child，Parent]
    # Не требует родительского контура


for i in range(len(contours)):
    print(i, contours[i])

# delete_list = []  # Создать список номеров контуров для удаления
# c, row, col = hierarchy.shape
# for i in range(row):
#     if hierarchy[0, i, 2] > 0 or hierarchy[0, i, 3] > 0:  # имеет родительский или дочерний контур
#         delete_list.append(i)
#
# contours_list = list(contours)
#
# # Удалить контуры, которые не соответствуют требованиям, согласно номеру списка
# contours = delet_contours(contours, delete_list)
#
# contours = tuple(contours_list)
#
# print(len(contours), "contours left after hierarchy filter")
# drawMyContours("contours after hierarchy filtering", image, contours, True)
