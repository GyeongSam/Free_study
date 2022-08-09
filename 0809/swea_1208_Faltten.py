for tc in range(1,11):
    N=int(input())
    L=list(map(int,input().split()))
    by_height=[0]*100   #높이에 따른 개수를 저장할 공간
    for i in range(100):    
        sub=[1]*L[i]+[0]*(100-L[i]) #개수를 높이에따라 나눠서
        for j in range(100):    #더해줌
            by_height[j]+=sub[j]

    top_sum=0   #위에서부터 더해갈 변수
    bot_sum=0   #아래서부터 더해갈 변수

    for top in range(99,0,-1):
        top_sum+=by_height[top]
        if top_sum>N:   #위에서부터 더하면서 N보다 커진다면 멈춤
            break
    
    for bot in range(0,100):
        bot_sum+=(100-by_height[bot])
        if bot_sum>N:
            break   #아래부터 더하면서 N보다 커지면 멈춤
    
    print(f'#{tc} {top-bot+1}') #출력


