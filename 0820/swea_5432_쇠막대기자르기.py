for T in range(1,int(input())+1):
    L=input()
    laser_list=[]
    sub=[]
    bar_list=[]
    cnt=0
    for i in range(len(L)-1):
        if L[i:i+2]=='()':
            laser_list.append(i)
    for i in range(len(L)):
        if i in laser_list or i-1 in laser_list:continue
        if L[i]=='(':
            sub.append(i)
        elif L[i]==')':
            bar_list.append([sub.pop(),i])
    for bar in bar_list:
        cnt+=1
        for laser in laser_list:
            if bar[0]<laser<bar[1]:
                cnt+=1
    print(f'#{T} {cnt}')
            

    