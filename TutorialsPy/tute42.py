import time
initial = time.time()
# print(initial)

i = 0
while i<=50:
    print("Iam Krushna Dike")
    i += 1
print(f"This is while loop ran time {time.time() - initial} seconds")

initial2 = time.time()
for i in range(50):
    print("Iam Krushna Dike")
print(f"This is for loop ran time {time.time() - initial2} seconds")