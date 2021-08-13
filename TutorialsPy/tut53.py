class Student:
    pass

harry = Student()   #Instances
larry = Student()   #Instances

harry.name = "Krushna"      #Instance variable
harry.std = 12
harry.session = 1
larry.std = 9
larry.sub = ["Hindi", "Marathi", "English"]
print(harry, larry)
print(harry.session, larry.std, larry.sub)
