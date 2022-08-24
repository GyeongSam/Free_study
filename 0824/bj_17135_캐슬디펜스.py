def find_Enmy(I,J):
    for d in range(D):
        for dx in range(-d,d+1):
            c_i=-(d+1)+abs(dx)+I
            c_j=J+dx
            if 0<=c_j<M and -N<=c_i<0 and Enmy_list[c_i][c_j]==1 and (c_i,c_j) not in kill:
                return c_i,c_j
    return 0

N,M,D=map(int,input().split())
Enmy_list=[list(map(int,input().split())) for _ in '_'*N]
R=[i for i in range(M)]
ARC_list=[[]]
for _ in '___':
    sub=[]
    for ARC in ARC_list:
        for r in R:
            if ARC==[] or r > ARC[-1]:sub.append(ARC+[r])
    ARC_list=sub[:]

max=0
for ARC in ARC_list:
    kill=[]
    total=0
    for i in range(N):
        target={0}
        for arc in ARC:
            target.add(find_Enmy(-i,arc))   
        target.discard(0)
        for ii,jj in target:kill.append((ii,jj))
        total+=len(target)
    if total>max:max=total
print(max)


# def find_Enmy(I,J):
#     for d in range(D):
#         for i in range(-d,d+1):
#             c_i=-(d+1)+abs(i)+I
#             c_j=J+i
#             if 0<=c_j<M and -N<=c_i<0 and Enmy_list[c_i][c_j]==1:
#                 return c_i,c_j
#     return 0

# N,M,D=map(int,input().split())
# Enmy_list=[list(map(int,input().split())) for _ in '_'*N]

# ARC_list=[]

# M=0
# for ARC in ARC_list:
#     total=0
#     for i in range(N):
#         target={0}
#         for arc in ARC:
#             target.add(find_Enmy(i,arc))
#         print(target)      
#         total+=len(target)-1
#     if total>M:M=total
