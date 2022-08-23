
D=[(0,1),(-1,0),(1,0),(0,-1)]   #이동방향

def chk(I,J):   #갈수 있는지 체크
    C=M[I][J]
    if C==0: return 1
    return 0
for T in range(1,int(input())+1):
    N=int(input())
    M=[[1]*(N+2)]+[[1]+list(map(int,input()))+[1] for _ in '_'*N]+[[1]*(N+2)]   #밖으로 나가지 않도록 1로 둘러쌈
    stk=[(l,k) for l in range(N+2) for k in range(N+2) if M[l][k]==2]   #스택 & 처음 위치
    visit=[] #방문목록
    G=0 #도착 여부
    while stk!=[]:  #스택이 빌때까지
        i,j=stk.pop()   #뽑음
        visit.append((i,j)) #방문처리
        for di,dj in D: #각방향을
            I,J=i+di,j+dj   #변수에 저장
            if M[I][J]==3:  #도착점이 있다면
                print(f'#{T} 1')    #도착 표시 후 종료
                G=1
                break
            if (I,J) not in visit and chk(I,J): #방문하지 않은 곳이고 갈 수 있는 곳이라면
                stk.append((I,J))   #스택에 넣고 다음으로
        else: continue
        break
    if G!=1:print(f'#{T} 0')



