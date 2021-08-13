def getdate():
    import datetime
    return datetime.datetime.now()

def log():
    # Harry
    if n2 == 1:
        print("Which data you want to log\n"
              "Press 1 for Diet\n"
              "Press 2 for Exercise :")
        n3 = int(input())
        if n3 == 1:
            with open("HarryDI.txt","a") as f:
                text = input("Type Here :\n")
                f.write(str([str(getdate())])+":"+text+"\n")
                print("Written Successfully...!")
        elif n3 == 2:
            with open("HarryEX.txt", "a") as f:
                text = input("Type Here :\n")
                f.write(str([str(getdate())]) + ":" + text+"\n")
                print("Written Successfully...!")
        else:
            print("Error!, pleas check your input")

    # Rohan
    elif n2 == 2:
        print("Which data you want to log\n"
                "Press 1 for Diet\n"
                "Press 2 for Exercise :")
        n3 = int(input())
        if n3 == 1:
            with open("RohanDI.txt", "a") as f:
                text = input("Type Here :\n")
                f.write(str([str(getdate())]) + ":" + text+"\n")
                print("Written Successfully...!")
        elif n3 == 2:
            with open("RohanEX.txt", "a") as f:
                text = input("Type Here :\n")
                f.write(str([str(getdate())]) + ":" + text+"\n")
                print("Written Successfully...!")
        else:
            print("Error!, pleas check your input")

    # Nikhil
    elif n2 == 3:
        print("Which data you want to log\n"
              "Press 1 for Diet\n"
              "Press 2 for Exercise :")
        n3 = int(input())
        if n3 == 1:
            with open("NikhilDI.txt","a") as f:
                text = input("Type Here :\n")
                f.write(str([str(getdate())])+":"+text+"\n")
                print("Written Successfully...!")
        elif n3 == 2:
            with open("NikhilEX.txt", "a") as f:
                text = input("Type Here :\n")
                f.write(str([str(getdate())]) + ":" + text+"\n")
                print("Written Successfully...!")
        else:
            print("Error!, pleas check your input")

    else:
        print("Error!, pleas check your input")

def retrive():
    #Harry
    if n2 == 1:
        print("Which data you want to retrive\n"
              "Press 1 for Diet\n"
              "Press 2 for Exercise :")
        n3 = int(input())
        if n3 == 1:
            with open("HarryDI.txt", "rt") as f:
                print("Harry Diet Contains :\n",f.read())
        elif n3 == 2:
            with open("HarryEX.txt", "rt") as f:
                print("Harry Exercise Contains :\n",f.read())
        else:
            print("Error!, pleas check your input")

    # Rohan
    elif n2 == 2:
        print("Which data you want to retrive\n"
                  "Press 1 for Diet\n"
                  "Press 2 for Exercise :")
        n3 = int(input())
        if n3 == 1:
            with open("RohanDI.txt", "rt") as f:
                print("Rohan Diet Contains :\n", f.read())
        elif n3 == 2:
            with open("RohanEX.txt", "rt") as f:
                print("Rohan Exercise Contains :\n", f.read())
        else:
                print("Error!, pleas check your input")
    # Nikhil
    elif n2 == 3:
        print("Which data you want to retrive\n"
                  "Press 1 for Diet\n"
                  "Press 2 for Exercise :")
        n3 = int(input())
        if n3 == 1:
            with open("NikhilDI.txt", "rt") as f:
                print("Nikhil Diet Contains :\n", f.read())
        elif n3 == 2:
            with open("NikhilEX.txt", "rt") as f:
                print("Nikhil Exercise Contains :\n", f.read())
        else:
            print("Error!, pleas check your input")

    else:
        print("Error!, pleas check your input")


print("################# Helth Management System ##########################")
print("What you want to do,\n"
      "Press 1 for LOG the data\n"
      "Press 2 for Retrive the data :")
n1 = int(input())

if n1 == 1:
    print("Press 1 for Harry\n"
          "Press 2 for Rohan\n"
          "Press 3 for Nikhil :")
    n2 = int(input())
    log()

elif n1 == 2:
    print("Press 1 for Harry\n"
          "Press 2 for Rohan\n"
          "Press 3 for Nikhil :")
    n2 = int(input())
    retrive()

else:
    print("Error, pleas check your input")