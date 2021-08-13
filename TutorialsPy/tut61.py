class Employee:
    var = 8
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        print(f"The Employee name is {self.name}, salary is {self.salary} and role is {self.role}. No of leaves are {self.no_of_leaves}")

    @classmethod
    def changeleaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_slash(cls, string):
        data = string.split("/")
        return cls(data[0], data[1], data[2])

    @staticmethod
    def printgood(string):
        print(string + " is a good boy")

class Player:
    var = 9
    no_of_games = 4

    def __init__(self, aname, agame):
        self.name = aname
        self.game = agame

    def printdetails(self):
        print(f"The Player name is {self.name} and game is {self.game}")

class CoolProgramer(Player, Employee):
    languages = ["C++", "Python"]
    def printlang(self):
        print(self.languages)

harry = Employee("Harry", 1400, "Manager")
rohan = Employee("Rohan", 15400, "viceManager")
nikhil = Employee.from_slash("Nikhil/1400/Chashiers")

amit = Player("Amit", ["Cricket", "Football"])

karan = CoolProgramer("Karan", ["Cricket"])
karan.printlang()
karan.printdetails()
print(karan.var)
