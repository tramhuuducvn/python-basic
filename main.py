import cv2

pathA = r"./image/img_a.png"
pathB = r"./image/img_b.png"

imageA = cv2.imread(pathA)
imageB = cv2.imread(pathB)

imageC = cv2.bitwise_and(imageB, imageA, mask=None)

cv2.imshow("imageA", imageA)
cv2.imshow("imageB", imageB)
cv2.imshow("imageC", imageC)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
