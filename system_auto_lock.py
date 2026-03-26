import cv2
import time
import os

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

last_seen = time.time()

while True:
    ret, frame = cap.read()

    # 🔥 MIRROR EFFECT
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        last_seen = time.time()
        print("User Present", end="\r")
    else:
        print("No Face Detected...", end="\r")

    # Lock after 5 sec of no face
    if time.time() - last_seen > 5:
        print("\nLocking System 🔒")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        break

    cv2.imshow("Smart Lock System", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()