# dp 활용

T = int(input())
for t_case in range(1, T + 1):
    N = int(input())
    sequence = list(map(int, input().split()))
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print('#{} {}'.format(t_case, max(dp)))