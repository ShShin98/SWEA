def dfs(n, sum):
    global result
    if sum > K: # 합이 K보다 커져버린 경우 탈출
        return 
    if n == N: # 인덱스가 N일 경우
        if sum == K: result += 1 # 부분수열의 합이 K이면 카운트 1증가
        return
    
    dfs(n + 1, sum + numbers[n])
    dfs(n + 1, sum)

T = int(input()) 
for t_case in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = 0

    dfs(0, 0) # 인덱스 0부터 시작, sum도 0부터 시작

    print('#{} {}'.format(t_case, result))