
class Employee:

    #class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, age,pay, email="Bosstech@gmail.com"):
        self.first = first
        self.last = last 
        self.age = age 
        self.pay = pay
        self.email = email

        Employee.num_of_emps = Employee.num_of_emps + 1

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def fullname(self):
        return self.first + " " + self.last

    def canVote(self):
        if self.age < 20 : 
            return "Cannot vote "
        else: 
            return " Go and vote for your party"

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


    def __str__(self):
        return f"{self.first} , {self.last} , {self.email}"
            


employee1 = Employee("letlotlo", "Ratheko", 23, "percy.ratheko@gmail.com")

employee2 = Employee("Zoro", "Max",33,40000)
#print(employee2.__dict__)
#print(employee2.apply_raise())
#print(employee2.__dict__)

print(Employee.num_of_emps)