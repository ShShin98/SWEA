from itertools import combinations

T = int(input())
for t_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    coms = list(combinations(numbers,3))
    sum_coms = sorted([sum(c) for c in coms], reverse=True)
    sum_final = []

    for s in sum_coms:
        if s not in sum_final:
            sum_final.append(s)

    print(f'#{t_case} {sum_final[4]}')