#Instructions: Create a variable of any name and set it equal to 10.
#The first if statement should read: if 10 (but use our variable, not the number 10) is greater than 12, print out "10 is greater than 12"
#The second if/else should read: Else if 10 is greater than 11, print out "10 is greater than 11"
#The third if/else should read: Else if 10 is equal to 10, print out "10 is equal to 10"
#The else should read: Else print out "10 is less than 10"

def main():
    number = 10
    if number > 12:
        print(str(number) + "is greter than 12")
    elif number > 11:
        print(str(number) + "10 is greater tahn 11")
    elif number == 10:
        print(str(number) + " is eaul to 10")
    else:
        print("10 is ess than 10")

main()
