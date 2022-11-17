T = 10
for t_case in range(1, T + 1):
    n, str = input().split()
    stack = []

    for s in str:
        if stack and s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    
    print('#{} {}'.format(t_case, ''.join(stack)))