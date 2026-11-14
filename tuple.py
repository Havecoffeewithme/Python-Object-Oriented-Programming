
thistuple = ("apple", "banana", "cherry", "watermelon", "carrots", "apple")
print(thistuple)
print(thistuple.count("apple"))
if "apple" in thistuple:
    print("True ... ")

y = list(thistuple)

y.append("peanut butter")


print(y)

del y[0:2]

print(y)
