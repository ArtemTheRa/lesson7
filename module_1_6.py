my_dict = {"Artem" : 89996545656, "Dmitriy" : 89995644512, "Mihail" : 85646545458, "Igor" : 89956452323}
print(my_dict)
print(my_dict["Artem"])
my_dict.update({"Maxim" : 89996541235,
                "Anton" : 86546541232})
del my_dict["Mihail"]
print(my_dict.get("Mihail"))
print(my_dict.get(85646545458))
a = my_dict.pop("Igor")
print(a)
print(my_dict)

print(" ")

my_set = {1, 2, 3, 4, 5, 6, 1, 1, 2, 4, 7, 12, 5, 8}
print(my_set)
my_set.update([9, 89, 123, 2, 1])
my_set.discard(1)
print(my_set)