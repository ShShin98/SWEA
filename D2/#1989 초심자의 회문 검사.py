T = int(input())

for test_case in range(1, T + 1):
    word = input()
    reversed_word = word[::-1]
    result = 0

    if word == reversed_word:
        result = 1
    
    print('#{} {}'.format(test_case, result))