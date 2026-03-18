
#Ask the user to input 2 numbers
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter a number: "))

#Determine the quotient of the 2 numbers that's been inputted without decimal points
if num_2 != 0:
    quotient = num_1 // num_2
    print("The quotient of the two numbers is: ", quotient)