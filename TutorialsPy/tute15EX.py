print("Enter First No :")
n1 = int(input())
print("Enter Second No :")
n2 = int(input())
print("Choose Operator :")
op = input()

if n1==45 and n2==3:
    print("Multiplication is :",555)
elif n1==56 and n2==9:
    print("Addition is :",77)
elif n1==56 and n2==6:
    print("Division is :",4)
else:
    if op == "+":
        add = n1 + n2
        print("Addition is :", add)
    elif op == "-":
        sub = n1 - n2
        print("Substraction is :",sub)
    elif op == "*":
        mul = n1 * n2
        print("Multiplication is :",mul)
    elif op == "/":
        div = n1 / n2
        print("Division is :",div)
    else:
        print("Error..!Check your input")