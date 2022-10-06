a,b=map(int,input().split())
cl=cr=0
while a!=1 or b!=1:
    if a>b:a,b=a-b,b;cl+=1
    else: a,b=a,b-a;cr+=1
print(cl,cr)
