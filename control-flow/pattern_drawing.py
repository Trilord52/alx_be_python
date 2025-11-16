size = input("Enter the size of the pattern: ")
try:
    size = int(size)
    if size <= 0:
        print("Please enter a positive integer!")
        exit()
except ValueError:
    print("Invalid input! Enter a positive integer.")
    exit()
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print() 
    row += 1
