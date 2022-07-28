def lonely(list_par):
    return (
        [list_par[0]] #0번째 항은 무조건 들어가니 적어줍니다.
        +[list_par[i] for i in range(1,len(list_par)) if list_par[i]!=list_par[i-1]]
        ) #1항부터 list를 순회합니다. 해당 항의 값이 전의 항과 같지 않을 경우에만
        #리스트에 담아 반환합니다.

print(lonely([1, 1, 3, 0, 1, 1])) #[1, 3, 0, 1]
print(lonely([4, 4, 4, 3, 3])) #[4, 3]