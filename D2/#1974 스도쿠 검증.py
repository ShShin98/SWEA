T = int(input())

for test_case in range(1, T + 1):
    puzzle = []
    result = 1

    for _ in range(9):
        puzzle.append(list(map(int, input().split())))
    
    for i in range(9):
        numArr1 = []
        numArr2 = []
        for j in range(9):
            if puzzle[i][j] in numArr1:
                result = 0
            numArr1.append(puzzle[i][j])

            if puzzle[j][i] in numArr2:
                result = 0
            numArr2.append(puzzle[j][i])
    
    square = [0, 3, 6]
    for i in square:
        for j in square:
            numArr3 = []
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if puzzle[x][y] in numArr3:
                        result = 0
                    numArr3.append(puzzle[x][y])

    print('#{} {}'.format(test_case, result))