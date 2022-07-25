for i in range(1,11):
    a=input()
    S=[[int(j) for j in list(input())] for _ in range(16)]

    next_R=[[1,1]]
    goal=0
    
    while(len(next_R)>=1 and goal==0):
        def go(x,y):
            S[x][y]=1             
            if(S[x-1][y]==0):
                next_R.append([x-1,y])
            if(S[x][y-1]==0):
                next_R.append([x,y-1])
            if(S[x+1][y]==0):
                next_R.append([x+1,y])
            if(S[x][y+1]==0):
                next_R.append([x,y+1])

        x,y=next_R.pop()
        
        if(S[x][y+1]==3):
            goal=1
        if(S[x+1][y]==3):
            goal=1
        if(S[x][y-1]==3):
            goal=1
        if(S[x][y-1]==3):
            goal=1
            
        go(x,y)
        
    
    print("#{}".format(i),goal)
