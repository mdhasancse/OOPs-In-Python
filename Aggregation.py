class customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.city, self.address.pin,self.address.state)

class Address:
    def __init__(self,city,pin,state):
        self.city = city
        self.pin = pin
        self.state = state

add1 = Address('Bangalore',560100,'Karnataka')
# call to add1
cust = customer('Hasan','male',add1)  
cust.print_address()