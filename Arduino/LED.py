import serial
import time

ArduinoSerial = serial.Serial('com3', 9600)
time.sleep(2)
print('a')
print(ArduinoSerial.readline())

print("Enter 1 to turn ON LED and 0 to turn OFF LED")

while True:  # бесконечный цикл
    var = input()  # считываем данные от пользователя
    print("you entered", var)  # печатаем подтверждение ввода

    if var == '1':  # если значение равно 1
        ArduinoSerial.write(bytes([1])) # передаем 1
        print("LED turned ON",bytes([1]))
        time.sleep(1)

    if var == '0':  # если значение равно 0
        ArduinoSerial.write(bytes([0]))  # передаем 0
        print("LED turned OFF", bytes([0]))
        time.sleep(1)
