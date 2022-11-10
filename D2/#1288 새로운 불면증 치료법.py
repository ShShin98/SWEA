T = int(input())

for t_case in range(1, T + 1):
    n = int(input())
    numbers = [0] * 10
    i = 1

    while True:
        if sum(numbers) == 10:
            break

        count = str(n * i)
        
        for c in count:
            c = int(c)
            if numbers[c] == 0:
                numbers[c] = 1
        i += 1

    print('#{} {}'.format(t_case, count))