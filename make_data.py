import numpy as np
import cv2
import time
import os



# # Label: 
label = input("Enter label: ")
print(label)
cap = cv2.VideoCapture(1)

i=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None, fx=1, fy=1)

    # Hiển thị
    cv2.imshow('frame', frame)
    # Lưu dữ liệu
    if (i >= 50):
        print("The number of capture = ", i - 50)
        # Tạo thư mục nếu chưa có
        if not os.path.exists('../dataset/' + str(label)):
            os.mkdir('../dataset/' + str(label))
        cv2.imwrite('../dataset/' + str(label) + "/" + str(i - 50) + ".png", frame)
        i += 1
    else: 
        i += 1
    if (i > 450): 
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()