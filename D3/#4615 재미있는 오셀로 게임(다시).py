T = int(input())
for t_case in range(1, T + 1):
    N, M = map(int, input().split()) # 보드 변의 길이, 돌 놓는 횟수 입력
    arr = [[0] * (N + 1) for _ in range(N + 1)] # 보드 생성
    m = N // 2 # 중간점
    # 초기 돌 배치
    arr[m][m] = arr[m + 1][m + 1] = 2
    arr[m][m + 1] = arr[m+1][m] = 1

    for _ in range(M): # 돌 놓는 횟수만큼 반복
        si, sj, d = map(int, input().split())
        arr[si][sj] = d # 해당 위치에 돌을 놓음
        # 자신을 기준으로 주변 8방향 탐색
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)):
            r = []  # 뒤집을 후보
            for mul in range(1, N): # 해당 방향으로 1~N칸 까지
                ni, nj = si + di * mul, sj + dj * mul # 검사할 좌표
                if 1 <= ni <= N and 1 <= nj <= N: # 보드 범위 안일 경우
                    if arr[ni][nj] == 0: # 해당 위치에 돌이 없으면
                        break
                    elif arr[ni][nj] == d: # 같은 색의 돌이 있으면
                        while r: # 뒤집을 후보들마다
                            ti, tj = r.pop() # 좌표를 꺼냄
                            arr[ti][tj] = d # 해당 좌표의 돌을 뒤집음
                        break # 뒤집었으면 탈출
                    else: # 다른 색의 돌이 있으면
                        r.append((ni, nj)) # 뒤집을 후보에 추가
                else: # 보드 범위 밖일 경우 
                    break

    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print('#{} {} {}'.format(t_case, bcnt, wcnt))
