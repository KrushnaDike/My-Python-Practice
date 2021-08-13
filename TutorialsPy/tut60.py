class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"The Employee name is {self.name}, salary is {self.salary} ane role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_slash(cls, string):
        data = string.split("/")
        return cls(data[0], data[1], data[2])

    @staticmethod
    def printgood(string):
        print("This is a good",string)

class Programmer(Employee):
    no_of_holyday = 40

    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages

    def print_prog(self):
        return f"The Programmer name is {self.name}, salary is {self.salary} and role is {self.role}. The languages is {self.languages}"

harry = Employee("Harry", 455, "Manager")
rohan = Employee("Rohan", 255, "Vice-Manager")
sanket = Employee.from_slash("Sanket/855/co-ordinator")

nikhil = Programmer("Nikhil", 455, "Programmer", ["Python", "Css"])
amit = Programmer("Amit", 855, "Programmer", ["Python"])

# harry.printgood("Harry")
# print(nikhil.print_details())
print(nikhil.no_of_holyday)
