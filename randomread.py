# Define the calc function
def calc(file, total, line_num):

    # Calculate the total
    for line in file:
        num = int(line)
        line_num += 1
        total += int(num)

    # Convert the total to a string for display
    total = str(total)

    # Display the total and length of list
    print("Total = " + total)
    print(line_num, "numbers in the file")

# Define the main function
def main():

    # Try to run the file
    try:

        # Open the file for reading
        file = open("numbers.txt", 'r')

        # Asign the variables
        total = 0
        line_num = 0

        # Call the calc function
        calc(file, total, line_num)

    except:
        print("File not found")

# Call the main function
main()