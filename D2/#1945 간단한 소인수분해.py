T = int(input())

for t_case in range(1, T + 1):
    n = int(input())
    numbers = [2, 3, 5, 7, 11]
    result = [0] * 5

    i = 0
    while True:
        if i == 5:
            break

        if n % numbers[i] == 0:
            n //= numbers[i]
            result[i] += 1
        else:
            i += 1
            continue

    print('#{} {}'.format(t_case, ' '.join(map(str, result))))