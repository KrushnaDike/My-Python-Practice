# import inspect
#
# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@gmail.com"
#
#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     @property
#     def email(self):
#         if self.fname == None and self.lname == None:
#             return "Email is not set please set it using setter property"
#         return f"{self.fname}.{self.lname}@gmail.com"
#
#     @email.setter
#     def email(self, string):
#         print("Setting Now.....")
#         names = string.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]
#
#     @email.deleter
#     def email(self):
#         print("This email is now deleted")
#         self.fname = None
#         self.lname = None
#
# skill_f = Employee("Skill", "f")
# # print(skill_f.email)
#
# print(id("This is a String"))
# print(id("This is also a String"))
#
# print(dir("This is also a String"))
# print(dir(skill_f))
#
# print(inspect.getmembers(skill_f))