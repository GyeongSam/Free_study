
n=int(input())
s=0
for i in range(1,10000000):
    s+=i
    if s>=n:break
m=s-n
if i%2:
    print(f'{1+m}/{i-m}')
else: print(f'{i-m}/{1+m}')


