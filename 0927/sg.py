import pprint
def promising(i,j,v):
    if 0 <= i < n and 0 <= j < n:
        if 1 in v[i]:
            return 0

        for p in range(n):
            if v[p][j] == 1:
                return 0
        ni = i - 1
        pj = j + 1
        mj = j - 1

        while True:
            if 0 <= ni < n:
                if 0 <= pj < n:
                    if v[ni][pj] == 1:
                        return 0
                    else:
                        pj += 1

                if 0 <= mj < n:
                    if v[ni][mj] == 1:
                        return 0
                    else:
                        mj -= 1
                ni -= 1
            else:
                break

        return 1

    else:
        return 0


def checknode(i,j,v,cnt):
    global res
    if cnt == n:
        res += 1
    else:
        ni = i + 1
        for nj in range(n):
            if promising(i,j,v):
                
            if nj == j - 1 or nj == j or nj == j + 1:
                continue
            else:
                v[i][j] = 1
                checknode(ni,nj,v,cnt)

    if promising(i,j,v):
        cnt += 1
        if cnt == n:
            res += 1
        else:
            ni = i + 1
            for nj in range(n):
                if nj == j - 1 or nj == j or nj == j + 1:
                    continue
                else:
                    v[i][j] = 1
                    checknode(ni,nj,v,cnt)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    res = 0
    v = [[0] * n for _ in range(n)]
    checknode(0,0,v,0)
    print(f'#{tc} {res}')