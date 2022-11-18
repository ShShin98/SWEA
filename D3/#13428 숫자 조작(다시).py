from itertools import combinations

T = int(input())
for t_case in range(1, T + 1):
    N = list(input()) # 숫자 입력(위치를 바꾸기 위해 리스트 형태로 입력)
    index_N = [i for i in range(len(N))] # 인덱스를 가지고 있는 리스트(바꿀 인덱스 고르는데 사용)

    min_num = max_num = int(''.join(N)) # 최솟값, 최댓값

    for idx in combinations(index_N, 2): # 바꿀 2개의 위치를 뽑는 조합마다
        i, j = idx # 바꿀 위치
        N[i], N[j] = N[j], N[i] # 숫자 위치를 바꿈

        if N[0] == '0': # 0으로 시작하면
            N[i], N[j] = N[j], N[i] # 원래대로 돌려놓음
            continue 
        # 최솟값, 최댓값 저장
        min_num = min(min_num, int(''.join(N))) 
        max_num = max(max_num, int(''.join(N)))
        N[i], N[j] = N[j], N[i] # 원래대로 돌려 놓음

    print(f'#{t_case} {min_num} {max_num}')