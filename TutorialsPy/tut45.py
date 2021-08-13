import sklearn as sk
# print(sk.__version__)

# import sys
# print(sys.path)

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

import file1
print(file1.a)
file1.printjoke("This is me")

# from file1 import a   # Don't use This bcause it is not recomanded
# print(a)