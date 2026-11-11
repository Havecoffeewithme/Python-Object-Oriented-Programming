class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname + " " + self.lastname)

class Student(Person):
    def __init__(self, fname,lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


    def __str__(self):
        return f"{self.firstname} , {self.lastname}, {self.graduationyear}"


p1 = Person("Senzo", "Nkosi")
p1.printname()

s1 = Student("Charlie", "Townsend", 2028)
print(s1)