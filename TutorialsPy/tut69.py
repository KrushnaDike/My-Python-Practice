class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return "Email is not set please set it using setter property"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting Now.....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        print("This email is now deleted")
        self.fname = None
        self.lname = None

hindustani_suppoeter = Employee("Hindustani", "Supporter")

print(hindustani_suppoeter.email)

hindustani_suppoeter.fname = "US"

print(hindustani_suppoeter.email)

hindustani_suppoeter.email = "this.that@gmail.com"
# print(hindustani_suppoeter.fname)
# print(hindustani_suppoeter.lname)
print(hindustani_suppoeter.email)

del hindustani_suppoeter.email
print(hindustani_suppoeter.email)
