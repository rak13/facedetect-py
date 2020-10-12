# setup environment:
#
# install python3 and pip3
#
# install opencv:
#   pip install opencv-python
#
# Note:
#   - The folder in which this program is run, may get flooded with images
#     Adding a delay between storing images may avoid that!

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)
imageIndex = 0
while 1:
    ret, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        crop_img = img[y: y+h, x:x+w]
        cv2.imwrite("thumbnail"+str(imageIndex)+".png", crop_img)
        imageIndex += 1

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
