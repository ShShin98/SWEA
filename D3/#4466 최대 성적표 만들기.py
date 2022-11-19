T = int(input())
for t_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    print('#{} {}'.format(t_case, sum(arr[:K])))