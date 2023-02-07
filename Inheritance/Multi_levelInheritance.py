# In multi-level Inheritance. we have parent, child, grand-child relationship
class parent:
    def get_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

class child(parent):
    def get_age(self,age):
        self.age = age

    def show_age(self):
        return self.age

class grandChild(child):
    def get_gender(self,gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

ob = grandChild()
ob.get_name("Hasan")
ob.get_age(23)
ob.get_gender("male")

print(ob.show_name())
print(ob.show_age())
print(ob.show_gender())

# print(ob.show_name(),ob.show_age(),ob.show_gender())
