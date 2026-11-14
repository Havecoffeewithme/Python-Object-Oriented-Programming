
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
addVeggies("tomatoes")
addVeggies("cabbage")
addVeggies("morogo")
addVeggies("potatoes")

for i in range(len(veggies)):
    print(veggies[i])

print()
print("-----------------------------------------------------------")
print()

thislist = ["ap", "ban", "cher", "loc", "wat", "cre"]

i = 0 

while i < len(thislist):
    print(thislist[i])
    i = i + 1


print()
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []

for x in fruits:
    if "a" in x:
        #print("true")
        newlist.append(x)

print(newlist)

print()

fruits2 = ["Appla2", "banana2", "Cherry2", "kiwi2", "mango2"]
print()
print("\n second list 3 ")
secondlist3 = []

for x in fruits2:
    if x.endswith("a2"):
        secondlist3.append(x)

print(secondlist3)
print()
print("\n second list 4 ")
secondlist4 = []
for x in fruits2:
    if x[0].isupper():
        secondlist4.append(x)

print(secondlist4)

thelist2 = []

for x in fruits2:
    if x[0].islower():
        thelist2.append(x.upper())

print(thelist2)

thiss = [100, 50, 65, 82, 23]
thiss.sort()
print(thiss)

thiss2 = thiss.copy()

print(thiss2)