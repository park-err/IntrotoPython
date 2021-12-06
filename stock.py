def main():
    #Calculate final earnings

    ##Joe's stocks variables
    stocks = 2000.0
    stock_price = 40.00
    sale_price = 42.75
    spendings = stocks * stock_price
    sellings = stocks * sale_price

    ##Commission variables
    commission1 = spendings * .03
    commission2 = sellings * .03
    total_commission = commission1 + commission2

    ##Earnings
    gross = sellings - spendings
    net = gross - total_commission

    #Display the variables

    print("Joe paid", format(spendings, '.2f'), "for purchasing", int(stocks), "stocks at", format(stock_price, '.2f'), ".")
    print("First commission totaled", format(commission1, '.2f'), ".")
    print("Joe made", format(sellings, '.2f'), "for selling", int(stocks), "stocks at", format(sale_price, '.2f'), ".")
    print("Second commission totaled", format(commission2, '.2f'), ".")


    #Display earnings

    ##Display the gross earnings
    print("Joe made", format(gross, '.2f'), "gross.")

    ##Display the net earnings
    if net > 0 :
        print("Joe made a profit of", format(net, '.2f'), ".")
    else:
        print("Joe lost", format(net, '.2f'), ".")

#Call the main function

main()