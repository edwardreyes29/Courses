# demonstrate hashtable usage


# TODO: create a hashtable all at once
items1 = dict({"key1" : 1, "key2" : 2, "key3" : "three"})
print(items1)

# TODO: create a hashtable progressively
# these data structure can shrink and grow when needed
items2 = {} # creates an empty dictionary
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)


# TODO: try to access a nonexistent key
# print(items1["key6"])

# TODO: replace an item
items1["key2"] = "two"
print(items1)

print(items2.items())  # items2.items() givea items list
print()

# TODO: iterate the keys and values in the dictionary
for key, value in items2.items():
    print("Key: ", key, " value: ", value)
