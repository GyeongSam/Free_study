class Doggy:
    num_of_dogs=0
    birth_of_dogs=0

    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        Doggy.num_of_dogs+=1
        Doggy.birth_of_dogs+=1
    
    def __del__(self):
        Doggy.num_of_dogs-=1
    
    def bark(self):
        print('왈왈')
    
    def get_status():
        print(f'총 태어난 마리수 : {Doggy.birth_of_dogs}')
        print(f'현재 마리수 : {Doggy.num_of_dogs}')


