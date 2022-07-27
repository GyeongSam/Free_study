import random 

class pair:
    def __init__(self, List):
        self.List=List
    
    def pick(self, n):
        return random.sample(self.List,n)

    def match_pair(self):
        sub_list=self.List[:]
        random.shuffle(sub_list)
        X=[[sub_list[i],sub_list[i+1]] for i in range(0,len(sub_list)-1,2)]
        if len(sub_list)%2==1:
            X[0].append(sub_list[-1])
        return X
            
peoples=pair(['a','b','c','d','e','f','g'])
print(peoples.match_pair())