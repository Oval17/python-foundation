# OOP notes — classes, objects, inheritance, abstract classes, super(), overriding, polymorphism.
#
# Run: python3 oop/oop.py


# ---------------------------------------------------------------------------
# 1. Class, object, __init__, methods
# ---------------------------------------------------------------------------
# - A class is a blueprint; an object is an instance of a class.
# - __init__ runs on object creation and sets per-object (instance) attributes.
# - A class can live in its own file and be imported elsewhere:
#       from car import Car
# - An object bundles related attributes + methods, e.g. phone, cup, book.


class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model} ({self.year}, {self.color})")


car1 = Car("Lambo", 2024, "Red", False)
car1.drive()


# ---------------------------------------------------------------------------
# 2. Single inheritance
# ---------------------------------------------------------------------------
# - Child class reuses parent's __init__ and methods, can add/override its own.
# - Ex: Dog inherits name/age/speak from Animal.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is speaking")


class Dog(Animal):
    pass


animal1 = Animal("Tommy", 2)
animal1.speak()

dog1 = Dog("Sheru", 3)  # Dog gets Animal.__init__ and speak() for free
dog1.speak()


# ---------------------------------------------------------------------------
# 3. Multiple and multilevel inheritance
# ---------------------------------------------------------------------------
# - Multiple inheritance: one class inherits from two (or more) parents.
# - Multilevel inheritance: chain — child inherits from a class that itself
#   inherits from another class.


class Swimmer:
    def swim(self):
        print("Swimming")


class Walker:
    def walk(self):
        print("Walking")


class Duck(Swimmer, Walker):  # multiple inheritance
    pass


duck = Duck()
duck.swim()
duck.walk()


class Puppy(Dog):  # multilevel: Puppy -> Dog -> Animal
    pass


puppy = Puppy("Chotu", 1)
puppy.speak()


# ---------------------------------------------------------------------------
# 4. Abstract class
# ---------------------------------------------------------------------------
# - An abstract class cannot be instantiated; it is a base for other classes.
# - It declares abstract methods (no body) that child classes MUST implement.
# - Needs ABC as base + @abstractmethod decorator — the decorator alone
#   without ABC does nothing.


from abc import ABC, abstractmethod


class AbstractAnimal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        ...  # no implementation here; children must provide one


class Cat(AbstractAnimal):
    def speak(self):
        print(f"{self.name} says Meow")


cat1 = Cat("Kitty", 2)
cat1.speak()

# AbstractAnimal("Ghost", 1)  # TypeError: can't instantiate without speak()


# ---------------------------------------------------------------------------
# 5. super() — call the parent's constructor/methods from the child
# ---------------------------------------------------------------------------
# - Ex: Circle reuses Shape's color/is_filled setup, then adds radius.


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


circle1 = Circle("Red", True, 5)
print(circle1.area())


# ---------------------------------------------------------------------------
# 6. Method overriding
# ---------------------------------------------------------------------------
# - Child provides its own version of a parent method (same name + params).
# - Ex: Dog overrides Animal.speak with a dog-specific version.


class LoudDog(Animal):
    def speak(self):  # overrides Animal.speak
        print(f"{self.name} says Woof!")


loud_dog = LoudDog("Bruno", 4)
loud_dog.speak()


# ---------------------------------------------------------------------------
# 7. Polymorphism
# ---------------------------------------------------------------------------
# - Same method name behaves differently per object type.
# - Achieved via method overriding: one call site, many implementations.


for pet in (Dog("Sheru", 3), Cat("Kitty", 2), LoudDog("Bruno", 4)):
    pet.speak()  # each class's own speak() runs
