T = int(input())

for t_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    print('#{} {}'.format(t_case, ' '.join(map(str, numbers))))