p=[]
m=[]
for i in range(1,6):
    N=input(f'{i}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:')
    if N=='Done':
        break
    p.append(int(N[:N.find('%')]))
    m.append(int(N[N.find('%')+1:N.find('g')]))
    print(p,m)
P=sum([p[i]*m[i] for i in range(len(p))])/sum(m)
M=sum(m)
print(f'{round(P,1)}% {round(M,1)}g')