def change_fuits(x):
    X=list(x.split(','))
    new_X=[]
    for i in X:
        I=i.lower()
        if I[0:6]=='rotten':
            I=I[6:]
        new_X.append(I)
    return new_X

print(change_fuits('apple,rottenBanana,apple,RoTTenorange,Orange'))
