import cv2

path = r"./pitbull.jpg"

image = cv2.imread(path)
cv2.imshow("tai anh", image)
cv2.imwrite("pitpull-so-cute.png", image)

# cv2.waitKey()
B, R, G = cv2.split(image)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.waitKey()


def sayHello(name: str) -> str:
    message: str = "Hello " + name
    return message


class Student:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return self.name + " is " + str(self.age) + " years old"


student: Student = Student("DUC", 2)
print("hello {0} {1}".format(9, 20))
