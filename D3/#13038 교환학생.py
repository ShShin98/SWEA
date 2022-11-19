T = int(input())
for t_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 1000000

    for i in range(len(arr)):
        if arr[i] == 1:
            cnt = 0
            temp = 0
            j = i
            while True:
                temp += 1
                if arr[j] == 1:
                    cnt += 1
                if cnt == n:
                    result = min(result, temp)
                    break
                j += 1
                if j == len(arr):
                    j = 0

    print('#{} {}'.format(t_case, result))