
class Animal:
    def __init__(self,name):
        self.name = name
    def walk(self):
        print(f'{self.name}! 걷는다!')
    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def bark(self):
        print(f'{self.name}! 짖는다!')
    def run(self):
        print(f'{self.name}! 달린다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('꼽이')
dog.run() 
dog.bark() #run과 bark 부모클래스인 Animal에 존재하지않으므로 자식클래스에 선언해줍니다.

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly() # walk와 eat는 부모클래스에 존재하므로 fly만 따로 선언해줍니다.