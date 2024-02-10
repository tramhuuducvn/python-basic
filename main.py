import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('./image/image2.jpg')
print(result)
result = reader.readtext('./image/image3.jpg')
print(result)
result = reader.readtext('./image/image4.jpg')
print(result)
result = reader.readtext('./image/image5.jpg')
print(result)