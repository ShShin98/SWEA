T = int(input())

for test_case in range(1, T + 1):
    t_num = int(input())
    student = list(map(int, input().split()))

    temp = 0
    result = 0

    for i in range(0, 101):
        if student.count(i) >= temp:
            temp = student.count(i)
            result = i

    print('#{} {}'.format(t_num, result))