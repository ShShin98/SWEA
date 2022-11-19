import datetime

T = int(input())
for t_case in range(1, T + 1):
    D, H, M = map(int, input().split())
    D *= 24 * 60
    H *= 60
    
    result = D + H + M - 11 * 24 * 60 - 11 * 60 - 11
    if result < 0:
        result = -1
    print('#{} {}'.format(t_case, result))