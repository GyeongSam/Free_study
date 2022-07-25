T=int(input())
for test_case in range(1,1+T):
    V,E,A1,B1 = map(int, input().split())
    A=list(map(int, input().split()))
    mother=[]
    son=[]
    for i in range(len(A)):
        if (i%2==0):
            mother.append(A[i])
        elif (i%2==1):
            son.append(A[i])    #인풋받고 부모와 자식관계로 정렬
    

    def MtoS(x):    #부모에서 자식가는 함수
        if x in mother:
            sub=[i for i, v in enumerate(mother) if v == x]
            return [son[n] for n in sub]
        else:
            return []

    def StoM(x):    #자식에서 부모가는 함수
        if x not in son:
            return -1
        else:
            return mother[son.index(x)]


    A1_mother_root=[A1]
    B1_mother_root=[B1]
    a=A1
    b=B1

    while (True):
        a=StoM(a)
        if (a==-1):
            break
        A1_mother_root.append(a)    #A의 조상 탐색

    while (True):
        b=StoM(b)
        if (b==-1):
            break
        B1_mother_root.append(b)    #B의 조상 탐색 

    AB_root=[]
    for i in range(min(len(A1_mother_root),len(B1_mother_root))):
        A_sub=A1_mother_root.pop()
        B_sub=B1_mother_root.pop()
        if(A_sub==B_sub):
            AB_root+=[A_sub]
        else:
            break       #가장 가까운 공통 부모 색출

    AB_M=AB_root.pop()
    Tree_scale=[AB_M]
    SUB=[AB_M]
    sub=[]
    No=0
    while(No==0):
        for i in SUB:        
            sub+=MtoS(i)
        if(sub==[]):
            No=1
            SUB=[]
        else:
            SUB=sub
            sub=[]
        Tree_scale+=SUB #색출한 부모 자식들 집합.

    print("#{}".format(test_case),AB_M,len(Tree_scale))
