T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 며칠인지 입력
    price = list(map(int, input().split())) # 각 날의 매매가 입력
    
    sell_price = 0 # 최고가(팔 값)
    result = 0 # 이득

    for p in price[::-1]: # 맨 뒤에서부터 탐색
        if p >= sell_price: # 현재 가격이 최고가보다 크거나 같으면
            sell_price = p # 최고가를 변경
        else: # 현재 가격이 최고가보다 작으면
            result += sell_price - p # 판매(이익만큼 변수에 저장)
    
    print('#{} {}'.format(test_case, result))

    # https://itcrowd2016.tistory.com/87