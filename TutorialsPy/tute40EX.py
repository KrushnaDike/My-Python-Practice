import random
print("😎😊😊😎😊😎😊😊😎😊😎😊😊😎 Snake Water Gun 😎😊😊😎😊😎😊😊😎😊😎😊😊😎")
com_point = 0
user_point = 0
i = 10
while i>=1:
    list1 = ["s", "w", "g"]
    com_choice = random.choice(list1)
    user_choice = input("Enter Your Choice :\n")

    if com_choice == user_choice:
        print("Same...😅🤣")

    elif com_choice == "s" and user_choice == "w":
        com_point = com_point + 1
        print(f"Computer Choice is {com_choice} and User Choice is {user_choice}")
        print("+1 Computer..💻")

    elif com_choice == "w" and user_choice == "g":
        com_point = com_point + 1
        print(f"Computer Choice is {com_choice} and User Choice is {user_choice}")
        print("+1 Computer..💻")

    elif com_choice == "g" and user_choice == "s":
        com_point = com_point + 1
        print(f"Computer Choice is {com_choice} and User Choice is {user_choice}")
        print("+1 Computer..💻")

    elif com_choice == "w" and user_choice == "s":
        user_point = user_point + 1
        print(f"Computer Choice is {com_choice} and User Choice is {user_choice}")
        print("+1 User..🏡")

    elif com_choice == "g" and user_choice == "w":
        user_point = user_point + 1
        print(f"Computer Choice is {com_choice} and User Choice is {user_choice}")
        print("+1 User..🏡")

    elif com_choice == "s" and user_choice == "g":
        user_point += user_point + 1
        print(f"Computer Choice is {com_choice} and User Choice is {user_choice}")
        print("+1 User..🏡")

    else:
        print("plz check your input!🤷‍")
        break

    print(f"Your remaining {i-1} chances..😎\n")
    i -= 1

print("Computer points are :",com_point)
print("User points are :",user_point)
if com_point>user_point:
    print("You looser...😒😒😁")
elif com_point==user_point:
    print("Match Draw...😅😅")
else:
    print("You winner...✌✌😍")