class A:
    classvar1 = "Iam in class A"
    def __init__(self):
        self.var1 = "Iam in class A's constructor"
        self.classvar1 = "Instance varibale in class A"
        self.special = "Special"

class B(A):
    classvar1 = "Iam in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "Iam in class B's constructor"
        self.classvar1 = "Instance varibale in class B"
        # print(super().classvar1)

a = A()
b = B()

print(b.classvar1)
print(b.special)