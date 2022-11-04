T = int(input())

for t_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    numbers.sort()

    sumNum = sum(numbers[1:-1])
    avg = sumNum / (len(numbers) - 2)

    print('#{} {}'.format(t_case, round(avg)))