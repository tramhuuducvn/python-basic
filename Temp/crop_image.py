import cv2

pitbull = r'./image/pitbull.jpg'
image = cv2.imread(pitbull)

ax, ay = 190, 290
bx, by = 310, 380

copy = image[ay:by, ax:bx]

print(image.shape)

# cv2.imshow("Pitbull So Cute", copy)

cv2.imwrite(r'./image/pitbull_nose.jpg', copy)

cv2.waitKey(3000)