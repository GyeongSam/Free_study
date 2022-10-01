i=int;I=input;
A=i(I())
for _ in '_'*i(I()):
    B,C=map(i,I().split())
    A-=B*C
print('No' if A else 'Yes')