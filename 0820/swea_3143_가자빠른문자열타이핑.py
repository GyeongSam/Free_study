
for T in range(1,int(input())+1):
    A,B=input().split()
    b=len(B)
    i=b-1
    print(i)
    cnt=0
    while i<=len(A):
        print(f'시작i:{i}')
        for d in range(b):
            print(f'd:{d}')
            if A[i-d]!=B[-1-d]:
                print(A[i-d]==B[-1-d])
                for n in range(b):
                    print(f'n:{n}')
                    if A[i-d]==B[n]:
                        i+=b-n-1;break
                        print(f'B내에 있으면:{i}')
                else:i+=b;break
                print(f'B내에 없으면:{i}')
        else:cnt+=1;i+=b
        print(f'다 돌았는데 맞다면')


    print(cnt)
            

