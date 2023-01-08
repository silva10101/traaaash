import cv2


def loading_displaying_saving():
    img = cv2.imread('1.jpg')  # , cv2.IMREAD_GRAYSCALE
    cv2.imshow('girl', img)
    cv2.waitKey(0)
    #  cv2.imwrite('graygirl.jpg', img)
    print("Высота:" + str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    print("Количество каналов:" + str(img.shape[2]))
    (b, g, r) = img[0, 0]
    print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))
    img[0, 0] = (255, 0, 0)
    (b, g, r) = img[0, 0]
    print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))


def resizing(new_width=None, new_height=None, interp=cv2.INTER_LINEAR):
    img = cv2.imread('1.jpg')
    h, w = img.shape[:2]
    print(h, w)

    if new_width is None and new_height is None:
        return img

    if new_width is None:
        ratio = new_height / h
        dimension = (int(w * ratio), new_height)

    else:
        ratio = new_width / w
        dimension = (new_width, int(h * ratio))

    res_img = cv2.resize(img, dimension, interpolation=interp)
    cv2.imshow('girl', res_img)
    cv2.waitKey(0)

def cropping():
    img = cv2.imread('1.jpg')
    crop_img = img[10:450, 300:750]

# loading_displaying_saving()
#resizing(1920, 1024)

image = cv2.imread('1.jpg')
b, g, r = cv2.split(image)
cv2.imshow('blue', b)
cv2.waitKey(0)
cv2.imshow('green', g)
cv2.waitKey(0)
cv2.imshow('red', r)
cv2.waitKey(0)
