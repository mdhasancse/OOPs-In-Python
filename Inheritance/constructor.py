class employee:
    def __init__(self,name,age,gender,salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        # we can call other methods also inside the class 
        # self.employee_details()


    def employee_details(self):
        print("Name of the employee ", self.name)
        print("age of the employee ", self.age)
        print("gender of the employee ",self.gender)
        print("salary of the employee ",self.salary)

ob = employee("Nirmal",23,"male",30000)
ob.employee_details()

   