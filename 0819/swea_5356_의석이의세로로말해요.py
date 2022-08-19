for T in range(1,int(input())+1):
    L=list(zip(*[input()+' '*15 for _ in '_'*5]))
    a=[]
    for i in L:a+=[j for j in i if j!=' ']
    print(f'#{T} ',*a,sep='')


