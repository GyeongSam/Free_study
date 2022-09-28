
def pre_order(i,N):                     #전위 순회 함수입니다.
    if i>N:return
    pre_order_list.append(num_list[i])
    pre_order(2*i,N)
    pre_order(2*i+1,N)

def in_order(i,N):                      #중위 순회 함수입니다.
    if i>N:return
    in_order(2*i,N)
    in_order_list.append(num_list[i])
    in_order(2*i+1,N)

def post_order(i,N):                    #후위 순회 함수입니다.
    if i>N:return
    post_order(2*i,N)
    post_order(2*i+1,N)
    post_order_list.append(num_list[i])

def in_order_print(i,N):                #중위 순회로 정답을 출력할 함수입니다.
    if i>N:return
    in_order_print(2*i,N)
    print(max(pre_order_list[i],in_order_list[i],post_order_list[i]),end=' ')
    in_order_print(2*i+1,N)             #중위 순회를 하면서 전위,중위,후위 순회의 해당 차례 중 가장 큰 값을 출력합니다.

T=int(input())                  
for test_case in range(1,T+1):
    N=int(input())                  
    num_list=[i for i in range(N+1)]    #정점 번호 리스트를 만듭니다.

    pre_order_list=[0]                  #전위 순회 정보를 저장할 리스트입니다.
    in_order_list=[0]                   #중위 순회 정보를 저장할 리스트입니다.
    post_order_list=[0]                 #후위 순회 정보를 저장할 리스트입니다.

    pre_order(1,N)                      #전위 순회 리스트에 정보를 채웁니다.
    in_order(1,N)                       #중위 순회 리스트에 정보를 채웁니다.
    post_order(1,N)                     #후위 순회 리스트에 정보를 채웁니다.

    print(f'#{test_case}',end=' ')      #출력을 위해
    in_order_print(1,N)                 #출력 전용 중위 순회 함수를 호출합니다.
    print()
