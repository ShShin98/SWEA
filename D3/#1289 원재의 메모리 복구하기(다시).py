T = int(input())
for t_case in range(1, T + 1):
    original = list(map(int, input()))
    default = [0] * len(original)
    result = 0

    for i in range(len(original)):
        if original[i] != default[i]:
            for j in range(i, len(original)):
                default[j] = original[i]
            result += 1

    print('#{} {}'.format(t_case, result))