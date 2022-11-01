T = int(input())

for test_case in range(1, T + 1):
    str = input()

    result = 0
    for i in range(1, 11):
        if str[0:i] == str[i:i + i]:
            result = len(str[0:i])
            break
    
    print('#{} {}'.format(test_case, result))