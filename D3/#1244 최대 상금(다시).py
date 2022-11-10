def dfs(n):
    global ans

    if n == N:
        ans = max(ans, int(''.join(map(str, lst))))
        return
    
    # L개에서 2개를 뽑는 모든 조합(둘을 교환)
    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int(''.join(map(str, lst)))
            if (n, chk) not in v:
                dfs(n + 1)
                v.append((n, chk)) 
            
            lst[j], lst[i] = lst[i], lst[j] # 원래대로 돌려놔야함

T = int(input())

for t_case in range(1, T + 1):
    st, t = input().split()
    N = int(t)
    lst = []

    for ch in st:
        lst.append(int(ch))

    L = len(lst)
    ans = 0
    v = []

    dfs(0)
    print('#{} {}'.format(t_case, ans))