class Employee:
    no_of_leaves = 10
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetail(self):
        return f"The name is {self.name}, salary is {self.salary} and role is {self.role}. leave is {self.no_of_leaves}"

    @classmethod
    def change_leave(cls, newleave):
        cls.no_of_leaves = newleave

    @classmethod
    def for_slash(cls, string):
        return cls(*string.split("/"))

    @staticmethod
    def printgood(string):
        print("This is Good " + string)
        # return "This is Good\t" + string

harry = Employee.for_slash("Harry/Developer/4000")
rohoan = Employee("Rohan", "HTML Expert", 688877)
karan = Employee.for_slash("Karan/student/100")

rohoan.change_leave(48)

rohoan.printgood("Krushna")