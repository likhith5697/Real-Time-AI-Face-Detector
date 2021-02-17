import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier('default.xml')
# img = cv2.imread("C:/Users/DELL/Desktop/face detection/johnson1.jpeg")

# to capture video from webcam
webcam = cv2.VideoCapture(0)


# iterate forever over frames
while True:
    successful_frame_read, frame = webcam.read()

    # covert to greyscale

    greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


# detect faces
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

    for(x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),
                                                  randrange(256), randrange(256)), 10)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
webcam.release()


print("Code Completed")

"""
# detect faces


face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)


# draw rectangles around faces


for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256),
                                            randrange(256), randrange(256)), 10)


x, y, w, h = face_coordinates[]
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 10)

# print(face_coordinates)

# display the images with faces

cv2.imshow('johnson1', img)
cv2.waitKey()
"""


print("Code Completed")
