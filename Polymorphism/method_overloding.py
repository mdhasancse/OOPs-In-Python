# // In python methodoverloding does not work. it will work java
# // A class has multiple methods having same name  but different in parameter

#*** It will call the method depend on input**

# Why we are use--> 
# bcs Increase readability of program. bcs(no need to write area_of_circle it 
# will understand depends on input which one i have to call)

class shape:

    def area(self,radius):
        return 3.14*radius*radius
    
    def area(self,l,b):
        return l*b
    
ob = shape()
ob.area(2)
ob.area(3,7)
