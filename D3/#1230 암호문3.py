T = 10
for t_case in range(1, T + 1):
    N = int(input())
    original = list(input().split())
    M = int(input())
    commands = list(input().split())

    for i in range(len(commands)):
        if commands[i] == 'I':
            idx = int(commands[i + 1])
            cnt = int(commands[i + 2])
            for j in range(cnt):
                original.insert(idx + j, commands[i + 3 + j])
        elif commands[i] == 'D':
            idx = int(commands[i + 1])
            cnt = int(commands[i + 2])
            del original[idx:idx + cnt]
        elif commands[i] == 'A':
            cnt = int(commands[i + 1])
            for j in range(cnt):
                original.append(commands[i + 2 + j])
    
    result = ' '.join(original[:10])
    print(f'#{t_case} {result}')