# Define the write function
def write(file, numbers):

    # Test the number to be within the range of 1 to 500
    if 1 <= numbers <= 500:

        # Write the list to the file
        file.write(str(numbers) + '\n')

    # Error message
    else:
        print("Error: Number is not within range of 1 and 500")


# Define the main function
def main():

    # Open/create the necessary file
    file = open("numbers.txt", 'w')

    # Ask user how many random numbers
    # the user would like to attach to the file
    how_many = int(input("How many numbers will be in the file:"))

    # Ask for all of the user's inputs
    for iteration in range(1, how_many + 1):

        # Ask for input and convert to integer
        numbers = int(input("Number between 1 and 500 #" + str(iteration) + ":"))

        #  Call write function
        write(file, numbers)

    # Close the file
    file.close()

# Call main function
main()
