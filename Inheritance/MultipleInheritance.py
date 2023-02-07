# // More than one parents class should be 

class parent1:
    def assign_string_one(self, str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1

class parent2:
    def assign_string_two(self, str2):
        self.str2 = str2

    def show_string_two(self):
        return self.str2

class Child(parent1, parent2):
    def assign_string_three(self, str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3
    
ob = Child()
ob.assign_string_one("I am String of parent 1")
ob.assign_string_two("I am String of parent 2")
ob.assign_string_three("I am String of child class ")
print(ob.show_string_one())
print(ob.show_string_two())
print(ob.show_string_three())
