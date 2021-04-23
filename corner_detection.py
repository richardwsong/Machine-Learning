#Richard Song
import cv2
import numpy as np


# filename = '1R4q1_8_8_1PpN4_1P2k3_8_N3pPPK_2R5.PNG'
# # filename = 'board1.jpg'
filename = 'board3.jpg'

im = cv2.imread(filename)
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

th, im_th = cv2.threshold(im_gray, 128, 190, cv2.THRESH_BINARY)

print(th)
# 128.0

cv2.imwrite('binarizedImage.jpg', im_th)

filename = 'binarizedImage.jpg'
# img = cv2.imread(filename)
#
#
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
#
# #result is dilated for marking the corners, not important
# dst = cv2.dilate(dst,None)
#
# # Threshold for an optimal value, it may vary depending on the image.
# img[dst>0.005*dst.max()]=[0,0,255]
#
#
# cv2.imshow('dst',img)
#
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
#
# cv2.imwrite('dst.jpg', img)

gray = cv2.imread(filename)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imwrite('edges-50-150.jpg',edges)
minLineLength=100
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)

a,b,c = lines.shape
for i in range(a):
    cv2.line(gray, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
    cv2.imwrite('houghlines5.jpg',gray)