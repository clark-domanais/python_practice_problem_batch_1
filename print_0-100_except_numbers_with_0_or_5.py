
#Print numbers from 0 to 100 except the numbers with 0 or 5 in them
for numbers in range(101):

#Check if the number contains 0 or 5
    if '0' not in str(numbers) and '5' not in str(numbers):
        print(numbers)
