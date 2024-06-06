def sqr(x):
    return x * x
    
def rec(x, y):
    return x * y
    
def tri(x, y):
    return 0.5 * x * y

print('Welcome to block calculations')

x = input("Enter the shape (triangle, square, or rectangle): ")

if x == "triangle":
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = tri(base, height)
elif x == "square":
    side = int(input("Enter the side of the square: "))
    area = sqr(side)
elif x == "rectangle":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = rec(length, width)
else:
    print("Invalid shape entered!")
    area = None

if area is not None:
    print("The area of the", x, "is:", area)
