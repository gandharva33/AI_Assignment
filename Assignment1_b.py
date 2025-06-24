n = int(input("Enter a number:")) # Ask the user to enter a number.

# To check if the number is less than or equal to 1
if n <= 1:
    print("The number should be greater than 1.") # Prime numbers are greater than 1

else:
    c = False # This will help us know if number is composite

    for i in range(2,n): # Loop through numbers from 2 to n
        if n%i == 0: 
            c = True     # Continue the loop if n is divisible by i

# If c is true then number is composite
if c:
    print("The given number is a composite number.") 

else:
    print("The given number is a prime number.") # If it isnt divisible then it means it is a prime number.              