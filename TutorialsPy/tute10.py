# Dictionary is nothing but the key-value pairs
d1 = {}
# print(type(d1))
d2 = {"Krushna":"Vadapav", "Sanket":"Icecream", "Shubhangi":"Roti",
      "Nikhil":{"B":"tea", "L":"Bhaji", "D":"Chicken"}}
# print(d2)

#Accessing dictionary element
# print(d2["Sanket"])

#Updating dictionary element
# d2["Kumar"] = "Chocklate"
# d2[420] = "Kababs"
# print(d2)
# or
# d2.update({"Kumar":"Chocklate"})
# print(d2)

#Deleting element from dictionary
# print("Before Deleting dictionary contain :",d2)
# del d2["Shubhangi"]
# print("After Deleting dictionary contain :",d2)

#Functions of dictionary
#1> copy()
# d3 = d2.copy()
# del d3["Nikhil"]
# print("dictionary d2 contain :",d2)
# print("dictionary d3 contain :",d3)

#2> get()
# print(d2.get("Sanket"))

#keys and values
print("Keys of Dictionary is :",d2.keys())
print("Values of dictionary is :",d2.values())