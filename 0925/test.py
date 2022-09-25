def ch(a,b):
    S=str(a)
    for i in range(len(S)):
        if int(S[i])<=b:
            S=S[:i]+str(b)+S[i:]
            break
    return int(S)
    
print(ch(75410,0))