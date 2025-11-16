number = input("Enter a number to see its multiplication table: ")
while not number.lstrip('-').isdigit():
    number = input("Invalid input! Please enter a valid number: ")
num = int(number)
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
