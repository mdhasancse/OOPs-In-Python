class private:
    def __init__(self):
        self.a = 10
        self._b = 20  #protected var
        self.__c = 30  # private var

    def showPrivateAttribute(self):
        return self.__c
    
    def Update_privateAttribute(self, value):
        self.__c = value

    def __private_method(self): #private method
        print("This is a private method")

        # call to private method
    def show_private_method(self):
        self.__private_method() 

obj = private()
obj.Update_privateAttribute(60)
print(obj.showPrivateAttribute())


obj.show_private_method()