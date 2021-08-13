class Employee:
    no_of_leves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}, salary is {self.salary} and the role is {self.role}, no_of_leves {self.no_of_leves}"

krushna = Employee("Krushna", 100000, "Computer Enginner")
nikhil = Employee("Nikhil", 1000000, "Civil Enginner")

# krushna.name = "Krushna"
# krushna.salary = 100000
# krushna.role = "Computer Enginner"
#
# nikhil.name = "Nikhil"
# nikhil.salary = 1000000
# nikhil.role = "Civil Enginner"
# nikhil.no_of_leves = 10

print(krushna.name)
print(nikhil.printdetails())