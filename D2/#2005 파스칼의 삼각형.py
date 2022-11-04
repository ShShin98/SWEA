T = int(input())

for t_case in range(1, T + 1):
    n = int(input())

    if n == 1:
        triangle = [[1]]
    elif n == 2:
        triangle = [[1], [1, 1]]
    else:
        triangle = [[1], [1, 1]]

        for i in range(1, n - 1):
            temp = []
            temp.append(1)
            for j in range (len(triangle[i]) - 1):
                nextNum = triangle[i][j] + triangle[i][j + 1]
                temp.append(nextNum)
            temp.append(1)
            triangle.append(temp)

    print('#', t_case, sep='')
    for line in triangle:
        print(' '.join(map(str, line)))