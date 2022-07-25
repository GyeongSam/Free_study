N=int(input())
L=[str(i).zfill(4) for i in range(0,10001)]
new_L=[]
for i in L:
    for j in range(len(i)+1):
        new_L.append(i[:j]+'666'+i[j:])
    
print(sorted(list(map(int, set(new_L))))[N-1])
