from customer import Customer

class Savings(Customer):
    def __init__(self, name : str, account : str, balance : float, branch : str ):
        self.__balance = balance
        super().__init__ (name, account, balance, branch)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, str):
            raise Exception("Balance cannot be String")
        else:
            self.__balance = value
    

#Customer.read_customers_from_csv()
#print(Customer.all)
Savings.read_customers_from_csv()
try:
    savings_cust1 = Savings("Chaitanya","Savings", 1000, "Hyderabad")
    print(Savings.all)
    savings_cust1.balance = 1234
    print(Savings.all)
except TypeError:
    print("Error occured during Item Assignment")

