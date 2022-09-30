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
        self.location= int(location)
        self.wallet= Wallet(money)

    def moveto(self, point):
        self.location = point
        
    def __strg__(self):
        print(f"you are located in {self.location}")



    # Implement the code here pass


person = Person("Moh", 5, 50)
person.moveto(10)


class Vendor(Person):
    
    def __init__(self, name, location, money,range, price):
        super().__init__(name, location, money) 
        price=1
        range=5
        self.range= range 
        self.price= price
    
    def sellTo(self, customer, number_of_icecreams):
        customer= Customer()
        self.location=customer.location
        amount= (number_of_icecreams * self.price)
        customerwallet= customer.money- amount 
        vendorwallet= self.money + amount 
 
        
    def __strg__(self): 
        print(f"you bought {self.number_of_icecream}ice cream")
        

            
        
vendor= Vendor("Abdallah", 3, 6,5,1)
vendor.sellTo(5,10)

class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)

    def _is_in_range(self,vendor):
        vendor=Vendor()
        rangefromvendor= vendor.location - self.location 
        if rangefromvendor <= 4:
            print("customer is within range")

    def _have_enough_money (self, vendor, number_of_icecreams):
        vendor= Vendor()
        if self.money >= (vendor.price * number_of_icecreams):
            print ("cutomer has enough money")
        else:
            print ("customer doesnt have sufficient amount")
    def _request_icecream(self, vendor, number_of_icecream )
        vendor=Vendor()
        customer=Customer()
        if customer._is_in_range and customer._have_enough_money:
            return ("request has been made")


    # implement Customer!
    pass


#customer = Customer("Abdallah", 3, 6)
