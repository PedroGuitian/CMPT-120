class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        if self.year > 2014:
            return("The car is less than a decade old")
        else:
            return("The car is old")
        
    #create your own function! what do you want it to do?
    
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Lope", 8)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("Nick", 1894, "Sales")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make
    newCake1 = Cake("Strawberry", "White")
    print(newCake1.flavor, newCake1.frosting)
    
    
    #and now create another cake and print it out
    newCake2 = Cake("Chocolate", "Brown")
    print(newCake2.flavor, newCake2.frosting)
    
    
    #create a cat!
    cat1 = Cat("Meatball", 12, "Short")
    print(cat1.name, cat1.age, cat1.fur_length)

    #create another cat!
    cat2 = Cat("Buck", 12, "Long")
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat2.name, cat2.age, cat2.fur_length)
    
    #create a car!
    car1 = Car("Mustang", 2015, "Silver")
    print(car1.model, car1.year, car1.color)
    #Now print out the function you made for car :)

main()
