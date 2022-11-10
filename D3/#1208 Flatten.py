T = 10

for t_case in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        max_index = box.index(max(box))
        min_index = box.index(min(box))

        box[max_index] -= 1
        box[min_index] += 1

    result = max(box) - min(box)

    print('#{} {}'.format(t_case, result))