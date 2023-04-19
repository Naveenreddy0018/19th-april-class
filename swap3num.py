a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if a > b and a > c:
    if b > c:
        temp = a
        a = c
        c = temp
    else:
        temp = 
        a = c
        c = temp
print(a, b, c)