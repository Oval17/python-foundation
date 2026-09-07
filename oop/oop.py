class Car:
    def __init__(self, model ,year, color , for_sale):
        self.model = model
        self.year = year 
        self.color = color 
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.model} car")
#we can put the class in seperate file as well and then from car import Car
#object is bundle of related attributes and methods ex phone , cup , book

car1 = Car("Lambo" , 2024 , "Red"  , False)

car1.drive()