# l = 8   #Global variable
# def function(n):
#     # l = 5     #Local variable
#     m = 10      #Local variable
#     global l    #Global keyword
#     l = l + 45
#     print(l, m)
#     print(n,"I have printed")
#
# function("This is me")
# # print(l)

x = 89
def krushna():
    x = 20
    def nikhil():
        global x
        x = 44
    print("Before calling nikhil() :", x)
    nikhil()
    print("After calling nikhil() :", x)

krushna()
print(x)