#Define pocket number colors

def isColor(num, color_num):

    if 0 < num <= 36:
        if 1 <= num <= 10:
            if color_num == 0:
                return "black"
            else:
                return "red"
        elif 11 <= num <= 18:
            if color_num == 0:
                return "red"
            else:
                return "black"
        elif 19 <= num <= 28:
            if color_num == 0:
                return "black"
            else:
                return "red"
        elif 29 <= num <= 36:
            if color_num == 0:
                return "red"
            else:
                return "black"
    else:
        return "green"

#Gather user information and compare to the color

def main():

    ##Assign user information to a variable

    num = int(input("Enter a pocket number: "))
    color_num = num % 2

    ##Display the pocket color

    if 0 <= num <= 36:
        color = isColor(num, color_num)
        print("The color of this pocket is", color)
    else:
        print("Error: This pocket number does not exist")

#Call main function

main()