T = int(input())

for t_case in range(1, T + 1):
    fh, fm, sh, sm = map(int, input().split())
    hResult, mResult = 0, 0

    hResult = fh + sh if fh + sh <= 12 else fh + sh - 12

    if fm + sm >= 60:
        mResult = fm + sm - 60
        hResult += 1
    else:
        mResult = fm + sm
    
    print('#{} {} {}'.format(t_case, hResult, mResult))