# // Method Overriding

# when both class have same method name then it willl call only child class of method

class phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self._price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    
class SmartPhone(phone):
    def buy(self):
        print("Buying a smart phone")

ob = SmartPhone(20000,"Apple",14)
ob.buy()