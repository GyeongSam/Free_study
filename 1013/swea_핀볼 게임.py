di=[0,1,0,-1]
dj=[1,0,-1,0]
for t in range(1,1+int(input())):
    N=int(input());ans=0
    field=[[5]*(N+2)]+[[5]+list(map(int,input().split()))+[5] for _ in '_'*N]+[[5]*(N+2)]
    hole = {6: [[], []], 7: [[], []], 8: [[], []], 9: [[], []],
            10: [[], []]}
    R=range(1,N+1)
    for i in R:
        for j in R:
            if field[i][j]>5:
                if hole[field[i][j]][0]:hole[field[i][j]][1]=[i,j]
                else: hole[field[i][j]][0]=[i,j]

    for i in R:
        for j in R:
            if field[i][j]==0:
                field[i][j] = -1
                for d in range(4):
                    ni=i;nj=j;c=d;s=0;
                    while(1):
                        ti = ni + di[c]
                        tj = nj + dj[c]
                        next = field[ti][tj]
                        if next == -1:
                            if s > ans: ans = s
                            break
                        if next == 0:
                            ni,nj,c,s=ti, tj, c, s
                        elif next == 1:
                            if c == 2:
                                ni, nj, c, s = ti, tj, 3, s+1
                            elif c == 1:
                                ni, nj, c, s = ti, tj, 0, s+1
                            elif c == 3:
                                ni, nj, c, s = ti, tj, 1, s + 1
                            else:
                                ni, nj, c, s = ti, tj, 2, s + 1
                        elif next == 2:
                            if c == 0:
                                ni, nj, c, s = ti, tj, 2, s + 1
                            elif c == 1:
                                ni, nj, c, s = ti, tj, 3, s + 1
                            elif c == 2:
                                ni, nj, c, s = ti, tj, 1, s + 1
                            else:
                                ni, nj, c, s = ti, tj, 0, s + 1
                        elif next == 3:
                            if c == 0:
                                ni, nj, c, s = ti, tj, 1, s + 1
                            elif c == 1:
                                ni, nj, c, s = ti, tj, 3, s + 1
                            elif c == 2:
                                ni, nj, c, s = ti, tj, 0, s + 1
                            else:
                                ni, nj, c, s = ti, tj, 2, s + 1
                        elif next == 4:
                            if c == 0:
                                ni, nj, c, s = ti, tj, 3, s + 1
                            elif c == 1:
                                ni, nj, c, s = ti, tj, 2, s + 1
                            elif c == 2:
                                ni, nj, c, s = ti, tj, 0, s + 1
                            else:
                                ni, nj, c, s = ti, tj, 1, s + 1
                        elif next == 5:
                            ni, nj, c, s = ti, tj, (c + 2) % 4, s + 1
                        elif next > 5:
                            if hole[next][0] == [ti, tj]:
                                ni, nj, c, s = hole[next][1][0], hole[next][1][1], c, s
                            else:
                                ni, nj, c, s = hole[next][0][0], hole[next][0][1], c, s
                field[i][j] = 0

    print(f'#{t}',ans)



