#  See why it will not execute or give error -->

# I called child class and child class have __init__ method, 
# it can access thier own init meth. and their attribute, it cannot call parent
# class method like-- *son.get_num* bcs it will not 
# go to parent __init__ method.  I am calling child class so thats why it 
# give error


# orr if you want to use parent __init__ method orr parameter then you have to use
# ****SUPER()*** method.

class parent:
    def __init__(self,num):
        self._num = num

    def get_num(self):
        return self._num

class child(parent):
    def __init__(self,val,num):
        self._val = val

    def get_val(self):
        return self._val


son = child(100,10)
print("Parent: Num: ",son.get_num)
print("Child Val: ",son.get_val)
