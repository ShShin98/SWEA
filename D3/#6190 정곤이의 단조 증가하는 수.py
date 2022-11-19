from itertools import combinations

def check(n):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True


T = int(input())
for t_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    comb = list(combinations(numbers, 2))
    result = -1

    for Ai,Aj in comb:
        num = Ai * Aj
        if num > result and check(num):
            result = num

    print(f'#{t_case} {result}')