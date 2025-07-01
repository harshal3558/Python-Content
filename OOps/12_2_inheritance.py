# Multi-Level Inheritance

class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyota(Car):
    def __init__(self,name):
        self.name = name

class Fortuner(Toyota):
    def __init__(self,type):
        self.type = type

car1 = Fortuner('diesel')
car1.start()