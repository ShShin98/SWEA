T = 10

for t_case in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))
    result = 0

    for i in range(2, n - 2):
        current = buildings[i]
        tallest = max(buildings[i - 1], buildings[i - 2], buildings[i + 1], buildings[i + 2])

        if current - tallest > 0:
            result += current - tallest

    print('#{} {}'.format(t_case, result))