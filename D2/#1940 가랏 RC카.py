T = int(input())

for t_case in range(1, T + 1):
    n = int(input())
    velocity = 0
    distance = 0

    for _ in range(n):
        command = list(map(int, input().split()))
        
        if command[0] == 1:
            velocity += command[1]
        elif command[0] == 2:
            velocity = 0 if command[1] > velocity else velocity - command[1]
        
        distance += velocity

    print('#{} {}'.format(t_case, distance))