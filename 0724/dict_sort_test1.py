A={'three':3, 'one':1, 'six':6, 'four':4, 'two':2, 'five':5}

B={}
for i in sorted(A.values()):
    for a,b in A.items():
        if i==b:
            B[a]=b

print(B)