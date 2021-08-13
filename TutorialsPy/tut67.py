class Employee:
    no_of_leaves = 34

    def __init__(self, aname, asalary, arole):
        self.name= aname
        self.salary= asalary
        self.role= arole

    def printdetails(self):
        return f"The name of Employee is {self.name} salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary / other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __pow__(self, other):
        return self.salary ** other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The name of Employee is {self.name} salary is {self.salary} and role is {self.role}"

emp1 = Employee("Krushna", 20, "Programmer")
emp2 = Employee("Nikhil", 2, "Tester")
print(repr(emp1))
print(emp1 // emp2)
print(emp1 * emp2)
print(emp1 ** emp2)
print(emp1 == emp2)