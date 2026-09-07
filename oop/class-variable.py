#class variable = shared among all instances of a class , defined outside of constructor allow us to share data among all objects created from that class

class student:

    def __init__(self , name , age):
        self.name = name
        self.age = age