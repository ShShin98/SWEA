code_of_num = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, 
               '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

T = int(input())
for t_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    pw_code = ''
    original_code = []

    for a in arr:
        if sum(a) == 0:
            continue
        else:
            for i in range(M - 1, -1, -1):
                if a[i] == 1:
                    pw_code = ''.join(map(str, a[i - 55:i + 1]))
                    break
            break
    
    for i in range(0, 56, 7):
        original_code.append(code_of_num[pw_code[i:i + 7]])
    
    answer = (original_code[0] + original_code[2] + original_code[4] + original_code[6]) * 3 + original_code[1] + original_code[3] + original_code[5] + original_code[7]

    if answer % 10 == 0:
        print('#{} {}'.format(t_case, sum(original_code)))
    else:
        print('#{} {}'.format(t_case, 0))