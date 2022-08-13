L=[];R=range(9)
for _ in R:
    L.append(int(input()))
S=sum(L)-100
for i in R[:-1]:
    for j in R[i+1:]:
        if L[i]+L[j]==S:
            L.pop(j)
            L.pop(i)
            break
    else:
        continue
    break
L.sort()
print(*L,sep='\n')
