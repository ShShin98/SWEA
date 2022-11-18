# 에라토스테네스의 체 이용하기

n = 1000001
isPrime = [True] * 1000002
isPrime[0] = isPrime[1] = False

for i in range(2, 1002):
    if isPrime[i]:
        for j in range(i * i, n + 1, i):
            isPrime[j] = False

for i in range(1, 1000002):
    if isPrime[i]:
        print(i, end=' ')