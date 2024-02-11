from easyocr import Reader
import cv2

def detect(img_path: str):
    # Reading and resizing the image
    img = cv2.imread(img_path)
    img = cv2.resize(img, (800, 600))
    # Convert image to grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)
    edged = cv2.Canny(blurred, 10 , 200)

    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    for c in contours:
        perimeter = cv2.arcLength(c, True)
        approximation = cv2.approxPolyDP(c, 0.02 * perimeter, True)
        # print(approximation)
        if len(approximation) == 4: # rectangle
            number_plate_shape = approximation
            break
        

    x, y, w, h = cv2.boundingRect(number_plate_shape)
    number_plate = grayscale[y:y + h, x:x + w]
    reader = Reader(['vi', 'en'])

    detection = reader.readtext(number_plate)

    if len(detection) == 0:
        return "Cannot detect plate number"
    else:
        return detection[0][1]