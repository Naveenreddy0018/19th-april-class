print("1.Area of the Triangle")
print("2.Area of the Square")
print("3.Area of the Rectangle")

ch = int(input("Enter your choice: "))

if ch == 1:
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    print("The area of the triangle is : ", 1/2*b*h)

if ch == 2:
    s = int(input("Enter side: "))
    print("The area of the square: ", s * s)

if ch == 3:
    l1 = int(input("Enter length: "))
    b1 = int(input("Enter breadth: "))
    print("The area of the rectangle: ", l1 * b1)
