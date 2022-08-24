R=[i for i in range(9)]

ARC_list=[[]]
for _ in '___':
    sub=[]
    for ARC in ARC_list:
        for r in R:
            if ARC==[] or r > ARC[-1]:sub.append(ARC+[r])
    ARC_list=sub[:]

print(ARC_list)