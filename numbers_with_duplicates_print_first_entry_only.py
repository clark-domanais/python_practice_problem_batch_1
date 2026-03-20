
#Ask user to input 10 numbers
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Display all numbers entered
print("\nAll numbers entered:")
print(numbers)

# Display numbers with only first occurrence of duplicates
print("\nNumbers with duplicates removed (first entry only):")
seen = set()
for num in numbers:
    if num not in seen:
        print(num, end=" ")
        seen.add(num)
print()  
