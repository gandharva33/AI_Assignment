n = int(input("Enter a number:"))

if n <= 1:
    print("The number should be greater than 1.")

else:
    c = False

    for i in range(2,n):
        if n%i == 0:
            c = True    

if c:
    print("The given number is a composite number.")

else:
    print("The given number is a prime number.")                