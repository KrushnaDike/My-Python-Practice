# Public
# Protected
# Private

class Employee:
    no_of_leaves = 8 #Public Variable
    _protec = 14 #Protected Variable
    __private = 50 #Private Variable

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

emp = Employee("Krushna", 1566, "Manager")
emp.printgood("Krushna")

print(emp._Employee__private) #Name Manglying