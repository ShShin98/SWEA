def dfs(c, v):
    global result
    result = max(result, len(v)) # 최대 이동 거리 저장

    for n in graph[c]: # 정점 c에 연결된 다른 정점
        if n not in v: # 방문한 적이 없으면
            dfs(n, v + [n]) # 방문 배열에 정점 추가, 이어서 방문

T = int(input())
for t_case in range(1, T + 1):
    N, M = map(int, input().split()) # 정점, 간선의 개수 입렵
    graph = [[] for _ in range(N + 1)] # 연결된 정점 저장할 리스트
    result = 0

    for _ in range(M): # 간선의 개수만큼 반복
        x, y = map(int, input().split()) # x, y는 연결
        graph[x].append(y)
        graph[y].append(x)

    for s in range(1, N + 1): # 1번부터 N번 정점까지 반복
        dfs(s, [s]) # s번 정점부터 출발, 방문 배열에 s번 정점 넣어서 전달
    
    print('#{} {}'.format(t_case, result))