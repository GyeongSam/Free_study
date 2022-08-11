def q_sort(L):  #퀵정렬
    if len(L)<=1:   #1미만시 그대로 리턴
        return L
    p,l=0,1
    r=len(L)-1
    while True:
        while L[l]<L[p]:    #왼쪽값이 피벗값보다 클때까지 오른쪽으로
            l+=1
            if l>len(L)-1:  #없다면 피벗값
                l=0
                break
        while L[r]>L[p]:#오른쪽값이 피벗값보다 작을때까지 오른쪽으로
            r-=1
        if l<r: #엇갈리지 않았다면
            L[l],L[r]=L[r],L[l] #교환
            l+=1
            r-=1
        else:   #엇갈렸다면
            L[p],L[r]=L[r],L[p] #왼쪽값과 피벗값 교환
            break
    return q_sort(L[0:r])+[L[r]]+q_sort(L[r+1:len(L)])  #왼쪽 부분과 오른쪽 부분을 또 퀵정렬

for tc in range(1,int(input())+1):
    N=int(input())
    L=list(map(int,input().split()))
    L=q_sort(L) #퀵정렬해서
    ans=[]  #답
    for i in range(5): #양쪽에서 하나씩 추가
        ans.append(L[-(i+1)])
        ans.append(L[i])
    print(f'#{tc} {" ".join(map(str,ans))}')





