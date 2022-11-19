# 방향 : 위,아래,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 탱크가 바라보는 곳
tank_pos = {'^': 0, 'v': 1, '<': 2, '>': 3, 0: '^', 1: 'v', 2: '<', 3: '>'}
# 입력된 이동 방향
command_dir = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

T = int(input())
for t_case in range(1, T + 1):
    H, W = map(int, input().split())
    game_map = [list(input()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if game_map[i][j] in ('<', '>', '^', 'v'):
                tank = (i, j, tank_pos[game_map[i][j]])  # 탱크의 좌표와 바라보는 곳
                break

    N = int(input())
    command = list(input())

    for c in command:
        if c == 'S':
            nx = tank[0]
            ny = tank[1]

            while True:
                nx += dx[tank[2]]
                ny += dy[tank[2]]
                if nx < 0 or nx >= H or ny < 0 or ny >= W or game_map[nx][ny] == '#':
                    break
                if game_map[nx][ny] == '*':
                    game_map[nx][ny] = '.'
                    break
        else:
            # 현재 탱크 위치
            x = tank[0]
            y = tank[1]
            # 이동할 탱크 위치
            nx = x + dx[command_dir[c]]
            ny = y + dy[command_dir[c]]
            game_map[x][y] = tank_pos[command_dir[c]]  # 탱크 방향 변경
            tank = (x, y, command_dir[c]) # 변경된 방향 최신화
            if 0 <= nx < H and 0 <= ny < W and game_map[nx][ny] == '.':
                game_map[x][y] = '.'
                game_map[nx][ny] = tank_pos[command_dir[c]]
                tank = (nx, ny, command_dir[c])

    print(f'#{t_case}', end=' ')
    for g in game_map:
        print(''.join(g))