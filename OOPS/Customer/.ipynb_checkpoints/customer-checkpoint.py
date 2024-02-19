import pandas as pd
class Customer:

    @classmethod
    def read_customers_from_csv(cls):
        data = pd.read_csv("customers.csv", sep = ",")
        print(data)


    def __init__(self, name, account, balance = 0, branch = ""):
        print("This method will call when class is initiated")
        self.name = name
        self.account = account
        self.balance = balance
        self.branch = branch
    

Customer.read_customers_from_csv()

# Initiating an object
cust1 = Customer("Chaitanya", "Savings", 1000, "Hyderabad")

# Printing the object attributes
print(cust1.name, cust1.account, cust1.balance, cust1.branch)

cust1.name = "Chaitanya Sagar"

# Printing the object attributes after update
print(cust1.name, cust1.account, cust1.balance, cust1.branch)