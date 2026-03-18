
#Ask the user to input 100 numbers 
numbers = []
for i in range(1, 101):
    numbers.append(i)
    
#Print the odd numbers from 1 to 100 using while loop
index = 0
while index < len(numbers):
    if numbers[index] % 2 != 0:
        print(numbers[index])
    index += 1