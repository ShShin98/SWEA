N = int(input())
result = []

for i in range(1, N + 1):
    num = str(i)
    clap = 0

    if '3' in num or '6' in num or '9' in num:
        clap += num.count('3') + num.count('6') + num.count('9')
        temp = '-' * clap
        result.append(temp)
    else:
        result.append(num)

print(' '.join(result))