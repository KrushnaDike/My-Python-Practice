# def function_name_students(a,b,c,d,e):
#     print(a,b,c,d,e)
# function_name_students("Krushna", "Nikhil", "Kumar", "Amit", "Kiran")

def funargs(normal, *args, **kwargs):
    # print(args[0])
    print(normal)

    for item in args:
        print(item)

    print("\nNow I would like to introduce some of our heroes :")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

std_name = ["Krushna", "Nikhil", "Kumar", "Amit", "Kiran", "Sonyabapu"]
normal = "Iam a normal Argument and the students are :"
kw = {"Krushna":"Programer", "Nikhil":"Developer", "Kumar":"Coordinator"}
funargs(normal,*std_name, **kw)


# dict = {"Krushna":"Programer", "Nikhil":"Developer", "Kumar":"Coordinator"}
# for item in dict:
#     print(item)