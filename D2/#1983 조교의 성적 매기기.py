T = int(input())

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t_case in range(1, T + 1):
    total_list =[]

    n, k = map(int, input().split())
    for _ in range(n):
        mid, final, hw = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + hw * 0.2
        total_list.append(total)

    k_score = total_list[k - 1]

    total_list.sort(reverse=True)

    score_group = n // 10

    k_score_group = total_list.index(k_score) // score_group

    print('#{} {}'.format(t_case, grades[k_score_group]))