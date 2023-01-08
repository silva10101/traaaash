import cv2

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap0 = cv2.VideoCapture(0)

while True:
    success, img0 = cap0.read()

    # img = cv2.imread("IMG_20191012_145410_3.jpg")
    img0_gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

    faces0 = face_cascade_db.detectMultiScale(img0_gray, 1.1, 19)

    for (x, y, w, h) in faces0:
        cv2.rectangle(img0, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('rez0', img0)

    # cv2.waitKey()
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap0.release()
cv2.destroyAllWindows()
