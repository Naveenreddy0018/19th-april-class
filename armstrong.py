n = int(input("Enter a number: "))
sum = 0
temp = n
l = len(str(n))
while n > 0: 
    rem = n % 10
    sum = sum + pow(rem, l)
    n = n // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an armstrong number")