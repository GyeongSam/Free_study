class Stack:
    def __init__(self):
        self.space=[]
    
    def empty(self):
        if self.space == []:
            return True
        else:
            return False
    
    def top(self):
        if self.space == []:
            return None
        else:
            return self.space[-1]
    
    def pop(self):
        if self.space == []:
            return None
        else:
            self.space,rest_num = self.space[:-1],self.space[-1]
            return rest_num
    
    def push(self,N):
        self.space+=[N]
    
    def __repr__(self):
        return f'{self.space}'
