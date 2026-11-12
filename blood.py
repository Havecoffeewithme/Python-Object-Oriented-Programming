import os

name = input("Enter a name of the file to delete : ")

if os.path.exists(name):
    os.remove(name)
    print(f"file : {name} - successfully deleted")
else:
    print(f"file {name} : does not exist")

# os.rmdir("name")

