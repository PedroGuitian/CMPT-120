def main():

    '''ask the user for their age. If the user is 25 or older, tell them they can buy alcohol, nicotine products, and they can rent a car
        If they're 21 or older but younger than 25, tell them they can buy alcohol, nicotine products, and they can rent a car
        If they're 18 and older but younger than 21, tell them they can only buy nicotine products in some states
        If they're less than 18, they can only purchase candy cigarettes and sody pops
    '''

name = input("How old are you? ")
if int(name) >= 25:
      print("you can buy alcohol, nicotine products, and they can rent a car")
elif 25 < int(name) > 21:
    print("you can buy alcohol, nicotine products, and they can rent a car")
elif 21 < int(name) > 18:
    print("you can only buy nicotine products in some states")
else:
    print("you can only purchase candy cigarettes and sody pops")
  
  
  
main()
