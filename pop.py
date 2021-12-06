#Calculate the population growth per day

def calc(population, percentage, total_days):

    total_days += 1
    for day in range(2, total_days):
        growth = population * percentage
        population += growth

        #Display the growth for the day and return to loop

        print("Day:", day, "Population:", population)
        day += 1

#Get user information and run the variables through the calculation function

def main():

    #Assign the variables to the user's information

    population = float(input("Starting number of organisms:"))
    percentage = float(input("Average daily increase percentage:")) / 100.0
    total_days = int(input("Number of days:"))

    ##Display the population of the first day

    print("Day: 1 Population:", population)

    ##Run variables through calculator function

    calc(population, percentage, total_days)

#Call main function

main()