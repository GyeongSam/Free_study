

def minlen(A,ans_list):
    ls=[]
    for i in ans_list:
        sub=len(A)
        for l in range(len(A)):
            if w[i][l]==A[l]:
                sub-=1
        ls.append(sub)
    return min(ls)

def BT(WORD,sum):
    global MAX
    cnt=[0]*26
    if not WORD:
        if sum<MAX:MAX=sum
    if sum > MAX:return
    for i in range(len(WORD)):
        cnt[ord(WORD[i])-97]+=1
        if cnt in cnt_w:
            ans_list=[]
            for n in range(N):
                if cnt_w[n]==cnt:ans_list.append(n)
            BT(WORD[i+1:],sum+minlen(WORD[:i+1],ans_list))
    else:
        return


MAX=1e10
W=input()
N=int(input())
w=[input() for _ in '_'*N]

cnt_w=[]

for ww in w:
    cnt_sub=[0]*26
    for www in ww:cnt_sub[ord(www)-97]+=1
    cnt_w.append(cnt_sub)

BT(W,0)
if MAX==1e10:MAX=-1
print(MAX)
