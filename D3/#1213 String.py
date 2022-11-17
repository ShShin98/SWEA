T = 10
for t_case in range(1, T + 1):
    t = int(input())
    str = input()
    sentence = input()

    result = sentence.count(str)
    print('#{} {}'.format(t_case, result))