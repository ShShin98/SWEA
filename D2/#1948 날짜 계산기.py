T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t_case in range(1, T + 1):
    fm, fd, sm, sd = map(int, input().split())
    result = 0

    for i in range(fm, sm + 1):
        if i == fm:
            result += days[fm] - fd + 1
        elif fm < i < sm:
            result += days[i]
        else:
            result += sd
    
    print('#{} {}'.format(t_case, result))