#first of all, breathe
#don't let this intimidate you. break it down a part at a time. You've done all of these separately and now we're just combining them.
'''
Instructions: Create a list with at least 8 numbers, and make sure you have a raandom dispersement between 0-50
Create a loop (which loop would be best given we know how long we're going [the length of the list]?) that runs through the entire list
Inside of your loop, have an if/elif/else that checks AT EACH INDEX OF THE LIST:
if the number is greater than 35: print ("greater than 35")
elif the number is between 20-35: print ("between 20-35")
elif the number is between 5-20: print ("between 5 and 20")
else (the number is less than 5)
'''
RandomNumbers = [1, 2, 3, 4, 5, 6, 8, 10]
# Loop through the entire list
for number in range(len(RandomNumbers)):
    if number > 35:
        print("Greater than 35")
    elif 20 <= number <= 35:
        print("Between 20-35")
    elif 5 <= number < 20:
        print("Between 5 and 20")
    else:
        print("Less than 5")

def main():

    main()
