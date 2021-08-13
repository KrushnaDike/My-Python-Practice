class A:
    def met(self):
        print("This is a method form class A")

class B(A):
    def met(self):
        print("This is a method form class B")

class C(A):
    def met(self):
        print("This is a method form class C")

class D(C, B):
    def met(self):
        print("This is a method form class D")

a = A()
b = B()
c = C()
d = D()

d.met()
