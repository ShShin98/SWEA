T = int(input())

for t_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = []
    for _ in range(n):
        puzzle.append(list(map(int, input().split())))
    
    result = 0
    cntH = 0
    cntV = 0
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 1:
                cntH += 1
            if puzzle[i][j] == 0 or j == n - 1:
                if cntH == k:
                    result += 1
                cntH = 0
            
            if puzzle[j][i] == 1:
                cntV += 1
            if puzzle[j][i] == 0 or j == n - 1:
                if cntV == k:
                    result += 1
                cntV = 0

    print('#{} {}'.format(t_case, result))