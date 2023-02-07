# In Hierarichical Only single parent class and others is child class

class phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self._price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    
class SmartPhone(phone):
    pass

class FeaturePhone(phone):
    pass

ob = SmartPhone(20000,"Apple","14px")
ob.buy()
print(" ")
ftr = FeaturePhone(10000,"One plus","25px")
ftr.buy()