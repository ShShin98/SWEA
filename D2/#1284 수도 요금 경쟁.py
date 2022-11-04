T = int(input())

for t_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    a_rates = P * W
    b_rates = Q if W <= R else Q + S * (W - R)

    print('#{} {}'.format(t_case, min(a_rates, b_rates)))