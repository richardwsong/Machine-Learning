# Richard Song

import cv2

filename = '1R4q1_8_8_1PpN4_1P2k3_8_N3pPPK_2R5.PNG'

im = cv2.imread(filename)
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

th, im_th = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY)

print(th)
# 128.0

cv2.imwrite('binarizedImage.jpg', im_th)