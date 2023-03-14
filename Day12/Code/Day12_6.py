# a1.__str__() will give a call to __str__() from Account class
# which is fetching some information from a1 object and displaying the details

class Account:
    def __init__(self,name,number,balance,id,email):
        self.name=name
        self.number=number
        self.balance=balance
        self.id=id
        self.email=email

    def __str__(self):
        return f"Number = {self.number} Balance = {self.balance}"

a1=Account("Akshita",1234,85000,999,"akshita@gmail.com")
print(f"A1 = {a1}") # a1.__str__() from Account class
print(f"dictionary of a1 = {a1.__dict__}")


