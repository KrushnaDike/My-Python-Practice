list1 = ["Bhindi", "Kobu", "Papad Masala", "Dangar"]

#here index start form 1
i = 1
for item in list1:
    if i%2 == 0:
        pass
    else:
    # if i % 2 != 0:
        print(f"Jarvice please buy {item}")
    i += 1


#here index start form 0
for index, item in enumerate(list1):
    if index%2 == 0:
        print(f"Jarvice please buy {item}")
