class Employee:
    no_of_leves = 8
    pass

krushna = Employee()
nikhil = Employee()

krushna.name = "Krushna"
krushna.sallary = 100000
krushna.role = "Computer Enginner"

nikhil.name = "Nikhil"
nikhil.sallary = 1000000
nikhil.role = "Civil Enginner"

print(Employee.no_of_leves)
print(nikhil.__dict__)
nikhil.no_of_leves = 10
print(Employee.__dict__)
print(nikhil.__dict__)
print(krushna.no_of_leves)