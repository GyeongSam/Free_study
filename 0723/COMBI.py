COMB_S=[]
for N in range(5,11):
    COMB_s=[[]]
    COMB_f=[]
    for _ in range(2,N+2):
        for i in range(len(COMB_s)):
            for j in range(2,N+2):
                if j not in COMB_s[i]: 
                    COMB_f.append(COMB_s[i]+[j])
        COMB_s=COMB_f
        COMB_f=[]
    COMB_S.append(COMB_s)