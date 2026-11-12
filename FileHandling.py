

"""
f = open("demofile.txt")
print(f.read())
f.close()

with open("demotabe.txt") as f:
        print(f.read())


with open("demofile.txt") as f:
    print(f.read(20))

"""


#with open("demo.txt") as f:
#    print(f.readline())
#    print(f.readline())

#with open("demo.txt") as f:
#    for x in f:
#        print(x)


#with open("demofile.txt", "a") as f:
#    f.write("Now we have a car to watch ")

#with open("demofile.txt") as f:
#    for x in f:
#        print(x)


with open("demofile.txt", "w") as f:
    f.write("Whoops! I have deleted the content")


with open("demofile.txt") as f:
    print(f.read())




with open("demo.tex") as file:
    for x in file:
        print(x)





