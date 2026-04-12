i = [15, 7, 22, 4, 16]

def sum_rev(arr, idx, total):
    if idx == len(arr):
        print(f'шаг суммы {idx+1}: total = {total}')
        return total
    total = total + arr[idx]
    print(f'шаг суммы {idx+1}: total = {total}')
    return sum_rev(arr, idx + 1, total)


def max_rev(arr, idx, cur_max):
    print(f'шаг максимума {idx+1}: cur_max = {cur_max}')
    if idx == len(arr):
        return cur_max
    if arr[idx] > cur_max:
        cur_max = arr[idx]
    return max_rev(arr, idx + 1, cur_max)

def min_rev(arr, idx, cur_min):
    print(f'шаг минимума {idx+1}: cur_min = {cur_min}')
    if idx == len(arr):
        return cur_min
    if arr[idx] < cur_min:
        cur_min = arr[idx]
    return min_rev(arr, idx + 1, cur_min)

mn = min_rev(i, 0, i[0])
print()
mx = max_rev(i, 0, i[0])
print()
sm = sum_rev(i, 0, 0)

print("\n" + "-"*25)
print('sum:', sm, 'min:', mn, 'max:', mx)
