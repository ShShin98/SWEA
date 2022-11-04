T = int(input())

for t_case in range(1, T + 1):
    n = int(input())
    original = ''

    for _ in range(n):
        c, k = input().split()
        original += c * int(k)

    print('#{}'.format(t_case))

    for i in range(0, len(original), 10):
        print(original[i:i + 10])