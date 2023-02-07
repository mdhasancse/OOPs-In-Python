from abc import ABC, abstractmethod
class BankApp(ABC):
    def database(delf):
        print("connected to database")

    @abstractmethod # decorator
    def security(self):# it is a abstract method bcs we use decorator @abstractmethod
        pass     # In abstract method we never give any kind of paramerter or anything simply pass

class MobileApp(BankApp):
    def mobile_login(self):
        print("log into mobile")

    def security(self):  # we have to give a method for security in child class
        print("mobile security")

ob = MobileApp()
ob.database()
ob.mobile_login()
ob.security()