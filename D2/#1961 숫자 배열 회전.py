T = int(input())

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ret[j][N - 1 - i] = m[i][j]
    
    return ret

def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ret[N - 1 - i][N - 1 - j] = m[i][j]
    
    return ret

def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ret[N - 1 - j][i] = m[i][j]
    
    return ret

for t_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    matrix_90 = rotate_90(matrix)
    matrix_180 = rotate_180(matrix)
    matrix_270 = rotate_270(matrix)

    print('#', t_case, sep='')
    for i in range(n):
        print(''.join(map(str, matrix_90[i])), ''.join(map(str, matrix_180[i])), ''.join(map(str, matrix_270[i])), sep=' ')
