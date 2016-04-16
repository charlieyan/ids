import ids
import cv2

cam = ids.Camera()
cam.continuous_capture = True
img, meta = cam.next()

cv2.namedWindow("Test", flags=cv2.WINDOW_NORMAL)
print (img.shape)
print str(meta)

K_QUIT      = ord('q')

while (1):
    cv2.imshow("Test",img)
    key = cv2.waitKey(1)
    key &= 0xFF # mask of 2^20
    if key == K_QUIT:
        break

cam.continuous_capture = False