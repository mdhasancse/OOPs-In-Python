# Encapsulation can be achieved using private var. and private method

# ****Remember
# _(Protected attributr) --> single underscore
# __(private attribute)  --> Double underscore

class student:
    __name = "Hasan"  #private varibale

    def __init__(self):
        print(self.__name)

        #we can't directly call private method, we have to call in constructor orr
        # or make other method and inside that we have to call
        self.__display()

    def __display(self): #private method
        print("This is private method")

obj = student()