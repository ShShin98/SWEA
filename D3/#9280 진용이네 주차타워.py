from collections import deque

T = int(input())
for t_case in range(1, T + 1):
    n, m = map(int, input().split())

    R_i = [int(input()) for _ in range(n)]
    check_R = [0] * n

    W_i = {}
    for i in range(1, m + 1):
        W_i[i] = int(input())
    
    queue = deque()
    result = 0
    full = True

    for _ in range(m * 2):
        car = int(input())
        if car > 0:
            for i in range(n):
                if check_R[i] == 0:
                    full = False
                    check_R[i] = car
                    result += W_i[car] * R_i[i]
                    break
                full = True
            if full:
                queue.append(car)
    
        elif car < 0:
            for i in range(n):
                if check_R[i] + car == 0:
                    check_R[i] = 0
                    if queue:
                        temp = queue.popleft()
                        check_R[i] = temp
                        result += W_i[temp] * R_i[i]
                    break

    print(f'#{t_case} {result}')