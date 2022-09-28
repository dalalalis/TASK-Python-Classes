class Wallet:
    def __init__(self,money):
        self.money= money

    def credit(self,amount):
        self.money += amount
        print (f"you have {self.money} remaing in wallet")

    def debit(self,amount):
        self.money -= amount
        f"you have {self.money} remaining in wallet"



wallet = Wallet(6)
wallet = Wallet(0)  # This should default money inside the wallet to 0
print(wallet)


class Person:
    def __init__(self, name, location, money):
        self.name= name
        self.location= location
        self.wallet= Wallet(money)

    def moveto(self, point):
        self.location = point
        print(f"you are located in {self.location}")



    # Implement the code here pass


person = Person("Moh", 5, 50)
person.moveto(10)

class Vendor(Person):
    def __init__(self, name, location, money,range, price):
        super().__init__(name, location, money) 
        self.range= range 
        self.price= price
    
    def sellTo(self, customer, number_of_icecreams):
        vendor= Vendor(Person)
        vendor.moveto(customer) 
        Vendor.wallet += (number_of_icecreams* self.price)
        print(f"you bought {number_of_icecreams} icecream")
            
        


    



    # implement Vendor!
    pass


vendor = Vendor("Abdallah", 3, 6,5,1)
vendor.sellTo(5,10)

class Customer:
    # implement Customer!
    pass


#customer = Customer("Abdallah", 3, 6)
