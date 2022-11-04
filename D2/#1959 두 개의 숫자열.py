T = int(input())

def calculate(A, B):
    result = 0

    for i in range(len(A) - len(B) + 1):
        temp = 0
        for j in range(len(B)):
            temp += B[j] * A[i + j]
        result = max(result, temp)

    return result

for t_case in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    maxSum = 0

    if n == m:
        for i in range(n):
            maxSum += a[i] * b[i]
    elif n < m:
        maxSum = calculate(b, a)
    else:
        maxSum = calculate(a, b)
    
    print('#{} {}'.format(t_case, maxSum))