from ast import Num
from os import NGROUPS_MAX


class Doggy:
    num_of_dogs=0
    birth_of_dogs=0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs+=1
        Doggy.birth_of_dogs+=1

    def bark(self):
        return ''
    
    def __del__(self):
        Doggy.num_of_dogs-=1

    def get_status():



