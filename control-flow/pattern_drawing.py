# pattern_drawing.py

# Propmt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in each column of the row
    for col in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Incriment row counter
    row += 1
