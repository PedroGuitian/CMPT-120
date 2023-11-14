#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

class student:
    def __init__(self, name, student_id, year, major, gpa):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.gpa = gpa

    def is_eligible_for_honors(self):
        return self.gpa > 3.5



student1 = student("John Doe", 123456, "Freshman", "Computer Science", 3.8)
student2 = student("Jane Smith", 789012, "Sophomore", "Mathematics", 3.2)

print(f"{student1.name} is eligible for honors: {student1.is_eligible_for_honors()}")
print(f"{student2.name} is eligible for honors: {student2.is_eligible_for_honors()}")
    
    
    
    
    
def main():
    #create three students and check if they get free lunch and if they qualify for honors
    def generate_and_check_id(student):
        # Generate a random student ID of the same length as the provided student's ID
        random_id = random.randint(10 ** (len(str(student.student_id)) - 1), 10 ** len(str(student.student_id)) - 1)

        # Check if the random ID matches the student's ID
        if random_id == student.student_id:
            print(f"Winner! {student.name} gets free lunch!")
        else:
            print("Loser!")
main()
