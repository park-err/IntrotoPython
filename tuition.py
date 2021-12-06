#Calculate the end tuition price

def tuition_amount(tuition, percentage):
    year = 0
    while year < 5:
        tuition += (tuition * percentage) / 100
        year += 1

    #Return the amount to the main function

    return tuition

#Gather user information

def main():

    #Assign user information to a variable

    tuition = int(input("Enter the tuition fee:"))
    percentage = int(input("Enter the increase as a percentage:"))

    #Put the user information into the calculator function

    total = tuition_amount(tuition, percentage)

    #Display the total tuition after 5 years

    print("Tuition total after 5 years: $" + format(total, '.2f'))

#Call the main function

main()