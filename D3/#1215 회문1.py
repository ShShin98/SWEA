T = 10
for t_case in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(8)]
    result = 0

    for i in range(8):
        for j in range(9 - N):
            word = board[i][j:j + N]
            if word == word[::-1]:
                result += 1
                
    for i in range(9 - N):
        for j in range(8):
            word = ''
            for n in range(N):
                word += board[i + n][j]
            if word == word[::-1]:
                result += 1

    print('#{} {}'.format(t_case, result))