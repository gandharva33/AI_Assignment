# Program to print the number of prime numbers given by the user
try:
    n = int(input("How many prime numbers do you want: "))  # Ask the user input for the number of prime numbers to be printed

    if n <= 0:
        print("Please enter a number greater than 0.")  # Checks if the number is less than or equal to 0
    else:               # Continues the loop if the number is greater than 0
        count = 0
        num = 2  

        print("Prime numbers are:")  # Prints the 'Prime numbers are:

        while count < n:  # Loop to find and print the first n prime numbers

            prime = True  # Assuming the number is prime initially

            for i in range(2, num):  # Loop to check if num is a prime number
                if num % i == 0:
                    prime = False

            if prime:  # If num is prime then it will be printed
                print(num)
                count += 1

            num += 1

        print("Total prime numbers printed:", count)  # Count of prime numbers to be printed.

except ValueError:
    print("Invalid input! Please enter a whole number like 5 or 10.")  # Exception handling for invalid input.


