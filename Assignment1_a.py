try:
    n = int(input("How many prime numbers do you want? "))

    if n <= 0:
        print("Please enter a number greater than 0.")
    else:
        count = 0       
        num = 2          

        print("Prime numbers are:")

        while count < n:
            
            prime = True
            for i in range(2, num):
                if num % i == 0:
                    prime = False

            if prime:
                print(num)
                count += 1
            num += 1  

        print("Total prime numbers printed:", count)

except ValueError:
    print("Invalid input! Please enter a whole number like 5 or 10.")