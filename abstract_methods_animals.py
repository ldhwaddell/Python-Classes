from abc import ABC, abstractmethod
class Animal(ABC):
 
    def move(self):
        pass
 
class Human(Animal):
 
    def move(self):
        print("I can walk and run")
 
class Snake(Animal):
 
    def move(self):
        print("I can crawl")
 
class Dog(Animal):
 
    def move(self):
        print("I can bark")
 
class Lion(Animal):
 
    def move(self):
        print("I can roar")
         
# Driver code
human = Human()
human.move()
 
snake = Snake()
snake.move()
 
dog = Dog()
dog.move()
 
lion = Lion()
lion.move()