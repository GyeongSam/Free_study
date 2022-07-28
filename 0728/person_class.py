
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def details(cls,name,years):
        cls.name=name
        cls.age=2022-years+1

    def check_age(self):
        return True if self.age>19 else False


p1=Person('ss',20)
print(p1.check_age())
