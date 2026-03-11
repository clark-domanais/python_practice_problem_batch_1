
#Ask the user to input 10 numbers 
numbers = []
for i in range(10):
    num = int(input("Please enter a number: "))
    numbers.append(num)

#Print how many the even numbers are from the list
even_numbers = [num for num in numbers if num % 2 == 0]
print("The number of even numbers is:", len(even_numbers))