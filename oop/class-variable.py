# Class variable notes.
#
# - A class variable is defined directly in the class body (outside __init__)
#   and is SHARED by all instances of that class.
# - Use it for data common to every object (e.g. graduation_year) or for
#   tracking class-level state (e.g. counting how many objects were created).
# - Access it via the class (Student.graduation_year) or any instance.
#
# Run: python3 oop/class-variable.py


class Student:
    graduation_year = 2024  # shared: same value for every student
    number_of_students = 0  # shared counter, bumped per new instance

    def __init__(self, name, age):
        self.name = name  # instance variable: unique per object
        self.age = age  # instance variable: unique per object
        Student.number_of_students += 1


student1 = Student("Anurag", 24)
student2 = Student("Ankit", 25)

# Class variable is identical for both instances:
print(student1.graduation_year)  # 2024
print(student2.graduation_year)  # 2024

# Instance variables differ per object:
print(student1.name)  # Anurag
print(student2.name)  # Ankit

# Counter was bumped once per __init__ call:
print(Student.number_of_students)  # 2
