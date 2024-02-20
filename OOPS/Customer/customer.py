import pandas as pd
class Customer:

    all = []
    customer_count = 0
    @classmethod
    def read_customers_from_csv(cls):
        data = pd.read_csv("customers.csv", sep = ",")
        #print(data)
        #print(len(data), data.loc[0]['name'])
        for i in range(len(data)):
            Customer(
                name = data.loc[i]['name'],
                account = data.loc[i]['account'],
                balance = float(data.loc[i]['balance']),
                branch = data.loc[i]['branch']
            )
        #print(all)    
        #print(data.loc[0]['account'])

    @staticmethod
    def is_float(balance):
        """Function to return if balance is float or not"""
        if isinstance(balance, float):
            return True
        elif isinstance(balance, int):
            return True
        else:
            return False

    def __init__(self, name, account, balance = 0, branch = ""):
        #print("This method will call when class is initiated")
        self.name = name
        self.account = account
        self.balance = balance
        self.branch = branch

        Customer.all.append(self)
        Customer.customer_count += 1
        

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.account}', {self.balance}, '{self.branch}')"
    
#Customer.read_customers_from_csv()
#print(Customer.all)
#print(Customer.customer_count)
#print(Customer.is_float(Customer.all[0].balance))