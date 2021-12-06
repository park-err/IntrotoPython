# Define main function
def main():
    # Assign variables

    acct_nums = []
    # # Opens the file of account numbers
    file = open('charge_accounts.txt', 'r')
    # # Converts the information to a list
    acct_nums = file.readlines()

    # Converts list of strings to list of integers
    for acct in range(0, len(acct_nums)):
        acct_nums[acct] = int(acct_nums[acct])

    # User will put in his/her account number
    user_num = int(input("What is your account number?: "))

    # User input will be verified with pre-existing list
    if user_num in acct_nums:
        print("Number is valid")
    else:
        print("Number is invalid")

# Call main function
main()

