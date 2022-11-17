T = 10
for t_case in range(1, T + 1):
    n = int(input())
    board = [input() for _ in range(100)]
    result = 1

    for l in range(2, 101):
        for i in range(100):
            for j in range(101 - l):
                word = board[i][j:j + l]
                if word == word[::-1]:
                    result = max(result, len(word))

        for i in range(101 - l):
            for j in range(100):        
                word = ''
                for d in range(l):
                    word += board[i + d][j]
                if word == word[::-1]:
                    result = max(result, len(word))

    print('#{} {}'.format(t_case, result))