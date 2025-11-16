number = input("Enter a number to see its multiplication table: ")
try:
    num = int(number)
except ValueError:
    print("Please enter a valid number!")
    exit()
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
