class phone:
    def set_color(self,color):
        self.color = color

    def set_cost(self,cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

    def make_call(self,):
        print("Making phone call")

    def play_game(self):
        print("playing game")

ob = phone()
ob.set_color("green")
print(ob.show_color())

ob.set_cost(100)
print(ob.show_cost())

ob.make_call()
ob.play_game()
