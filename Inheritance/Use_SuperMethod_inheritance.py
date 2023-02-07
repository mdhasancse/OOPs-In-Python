# How to use super fun --->

class vehicle:
    def __init__(self, milege,cost):
        self.milege = milege
        self.cost = cost

    def show_vehicle_details(self):
        print("malege of vehicle ", self.milege)
        print("cost of vehicle ", self.cost)
        print("I am vehcle")

# child class or sub class
class Car(vehicle):
    def __init__(self, milege,cost, tyres, model):
    # milage and cost are already in parant class of init method, so we will 
    # use super fun. in child class to access paraent properties 
        super().__init__(milege,cost)
        self.tyres = tyres
        self.model = model

    def show_Car_details(self):
        print("Number of tyres in car ",self.tyres)
        print("Model of the car ",self.model)
        print("I am a car")


c = Car(90,2000000,4,2022)
c.show_Car_details()
print(" ")

# can access parents properties alse
c.show_vehicle_details()

