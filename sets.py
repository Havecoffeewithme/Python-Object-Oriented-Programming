"""

thisset = {"apple", "banana", "cherry"}
#print(thisset)

#since we cant have duplicates or change the velue 
# we can add or remove items  
# use it when we want to store unique values 

if "apple" in thisset: 
    print("true")



thisset.add("oranges")
thisset.add("cherry")
thisset.add("tomatoes")

print()

for x in thisset:
    print(x)

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# remove() will cause an error if the item does not exit 
# then use discard


"""

set1 = {"aa", "bb", "cc"}
set2 = {"dd", "ee", "ff"}

set3 = set1.union(set2)

print(set3)

set3.discard("ff")

print(set3)

print(set1.intersection(set3))
