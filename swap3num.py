a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if a > b and a > c:
    if b > c:
        temp = a
        a = c
        c = temp
    else:
        temp = a
        a = b
        b = c
        c = temp

elif b > c and b > a:
    if c > a:
        temp = b
        b = c
        c = temp
    else:
        temp = b
        b = a
        a = c
        c = temp

else:
    if a > b:
        temp = b
        b = a
        a = temp
    
print(a, b, c)