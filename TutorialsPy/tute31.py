with open("krushna.txt") as f:
    a = f.readlines()
    print(a)

f = open("krushna.txt", "rt")
# print(f.readlines())
print(f.read(12))
f.close()