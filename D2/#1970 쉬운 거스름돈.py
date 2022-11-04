T = int(input())

for t_case in range(1, T + 1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0] * 8

    for i in range(len(money)):
        if n // money[i] == 0:
            continue
        else:
            result[i] = n // money[i]
            n = n % money[i]

    print('#{}'.format(t_case))
    print(' '.join(map(str, result)))
