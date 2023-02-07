# parant class or super class
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
    def show_car(self):
        print("I am a car")

# v1 = vehicle(70,100000)
# v1.show_vehicle_details()
# print("/") 

c = Car(90,200000)
c.show_vehicle_details()
print(" ")
c.show_car()