## Animal is-a object 
class Animal(object):
    pass

# Dog is-a Animal
class Dog(Animal):
    def __init__(self,name):
        #has-a
        self.name = name

# Person is-a Object
class Person(object):
    def __init__(self, name):
        #has-a
        self.name = name

        #has-a pet
        self.pet = None

# Employee is a person
class Employee(Person):
    def __init__(self,name,salary):
        #has-a name which is an attribute inherited from the Person class
        super(Employee,self).__init__(name)
        # has - a salary
        self.salary = salary

#Fish is an object
class Fish(object):
    pass

#Salmon is a Fish
class Salmon(Fish):
    pass

#Halibut is a Fish too
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is a person 
mary = Person("Mary")
mary.pet = satan

#frank is-a Employee with a salary of 120000
frank = Employee("Frank",120000)

# frank has-a pet named rover
frank.pet = rover

#flipper is a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

#harry is a Halibut
harry = Halibut()