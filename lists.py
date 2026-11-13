
"""
mylist = ["apple", "banana", "cherry", "tomatoes"]

for x in mylist:
    print(x, end=" ")

print(mylist[0] == "apple")
mylist.append("pineapple")
mylist.append("grapes")
print(mylist)
mylist.pop()
print(mylist)

#print(mylist[0:3])

print(len(mylist))

if "cherr" in mylist:
    print("Yes , cherry in the list")
else: 
    print("item not in the list")
print(mylist)
mylist.insert(2, "lemons")

print(mylist)

moFruits = ["carrots", "beetroot", "seeds"]

mylist.extend(moFruits)

print(mylist)

del mylist[0]

print(mylist)
"""
mylist = ["apple", "banana", "cherry", "tomatoes"]
moFruits = ["carrots", "beetroot", "seeds"]

mylist.extend(moFruits)

def remove( fruit):
    if fruit in mylist:
        mylist.remove(fruit)
        print(f"{fruit}, successfully removed")
    else: 
        print(f"{fruit} not available")


veggies = []

def addVeggies(fruit):
    if fruit not in veggies:
        veggies.append(fruit)
    else:
        print(f"{fruit} already in the basket")


addVeggies("spinash")
addVeggies("spinash")


print("\ncurrent fruits : ")
for v in veggies:
    print(v, end=" ")