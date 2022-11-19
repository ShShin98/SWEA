dic1 = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
        'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
dic2 = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR',
        5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

T = int(input())
for t_case in range(1, T + 1):
    t, n = input().split()
    arr = list(input().split())
    trans = [dic1[a] for a in arr]
    trans.sort()
    result = [dic2[t] for t in trans]
    
    print('#{}'.format(t_case))
    print('{}'.format(' '.join(result)))