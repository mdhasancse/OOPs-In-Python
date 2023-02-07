# By default python does not suppor abstract class 
# but we can achieve abstract classes by importing "abc" 
# ABC stand for --> Abstract Base Classs

from abc import ABC, abstractmethod

class Computer(ABC): # abstract class

    @abstractmethod # decorator
    def process(self):  # it is a abstract method bcs we use decorator @abstractmethod
        pass

class Laptop(Computer):
    def process(self): # we have to give a method for security in child class as same as parents method
        print("its running")

    

com = Laptop()
com.process()