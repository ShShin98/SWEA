T = 10
for t_case in range(1, T + 1):
    t = int(input())
    numbers = list(map(int, input().split()))

    while True:
        temp = 1
        for i in range(1, 6):
            if numbers[0] - i > 0:
                temp = numbers[0] - i
            else:
                temp = 0
            
            del numbers[0]
            numbers.append(temp)

            if temp == 0:
                break
        if temp == 0:
            break
    
    print('#{} {}'.format(t_case, ' '.join(map(str, numbers))))