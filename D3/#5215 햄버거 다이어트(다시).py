def dfs(i, score, cal): # 인덱스, 점수의 합, 칼로리의 합
    global result
    # 칼로리가 기준치를 초과하면 리턴
    if cal > L: 
        return
    # 점수가 현재 result보다 크면 대입
    result = max(result, score) 
    # 모든 재료를 탐색했다면 리턴
    if i == N: 
        return
    # 인덱스를 통해 현재 재료의 점수와 칼로리를 저장
    s, c = arr[i]
    # 현재 재료를 사용한 경우, 사용하지 않은 경우로 나눠서 dfs 탐색 
    dfs(i + 1, score + s, cal + c) # 사용 했으면 점수와 칼로리를 더함
    dfs(i + 1, score, cal) # 사용하지 않았으면 점수와 칼로리를 유지한 채로 다음 재료 탐색


T = int(input())
for t_case in range(1, T + 1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0 # 점수의 최댓값

    dfs(0, 0, 0) 

    print('#{} {}'.format(t_case, result))