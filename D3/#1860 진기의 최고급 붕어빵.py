T = int(input())
for t_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()
    result = 'Possible'
    fish = 0

    for i in range(time[len(time) - 1] + 1):
        if i > 0 and i % M == 0:
            fish += K
        
        if i in time:
            if fish == 0:
                result = 'Impossible'
                break
            else:
                fish -= 1
        
    print('#{} {}'.format(t_case, result))