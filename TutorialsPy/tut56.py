class Employee:
    no_of_leavs = 10

    def __init__(self, aname, arole, asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary

    def printdetails(self):
        return f"The name is {self.name}. and role is {self.role} and salary is {self.salary} and the no of leavs is {self.no_of_leavs}"

    @classmethod
    def change_leavs(cls, newleave):
        cls.no_of_leavs = newleave

harry = Employee("Harry", "Developer", 4555)
rohoan = Employee("Rohan", "HTML Expert", 688877)

harry.change_leavs(48)

print(Employee.no_of_leavs)