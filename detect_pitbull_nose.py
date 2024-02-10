import cv2

pitbull = cv2.imread(r'./image/pitbull.jpg')
pitbull = cv2.cvtColor(pitbull, cv2.COLOR_BGR2RGB)

pitbull_nose = cv2.imread(r'./image/pitbull_nose.jpg')
pitbull_nose = cv2.cvtColor(pitbull_nose, cv2.COLOR_BGR2RGB)


method = eval('cv2.TM_CCOEFF')
p_copy = pitbull.copy()

result = cv2.matchTemplate(p_copy, pitbull_nose, method)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

height, width, channel = pitbull_nose.shape
bottom_right = (top_left[0] + width, top_left[1] + height)
cv2.rectangle(pitbull, top_left, bottom_right, (0, 0, 255), 3)

# Show result
cv2.imshow("Pitbull", pitbull)


k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
    
    