
class Person:
    def __init__(self, name: str, address: str, phone_number: str, debt: int) -> None:
        self.name = name
        self.money = 0
        self.debt = 0
        self.address = address
        self.phone_number = phone_number
    def add_money(self, money: int) -> int:
        self.money += money
        return self.money
    def add_debt(self, debt: int) -> int:
        self.debt += debt
        return self.debt

class Person1(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

customers = []

while True:
    name = input("What is the customers name? : ")
    if name == "exit":
        break
    address = input("What is the customer address? : ")
    phone_number = input("What is the customers phone number? : ")
    money = int(input("How much money does he have? : "))
    debt = int(input("How much does he owe? : "))
    customer = Person(name, address, phone_number, debt)
    customer.add_debt(debt)
    customer.add_money(money)
    customers.append(customer)

print("-------------------------------------------------")
while True:
    name = input("What is the customers name you want to see? : ")
    customer = [customer for customer in customers if customer.name == name][0]
    print(f"{customer.name} owes {customer.debt}.\nHis information is:\nAddress: {customer.address}\nPhone Number: {phone_number}\nMoney: {customer.money}\nDebt: {customer.debt}\nMoney After Paying Debt: {customer.money - customer.debt}")
