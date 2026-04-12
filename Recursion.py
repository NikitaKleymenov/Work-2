# Сумма + Минимум + Максимум, всё через рекурсию, else быть не должно
i = [15, 7, 22, 4, 16]

def sum(i):
  if 0 < len(i):
    print(i[0])
    return i[0] + sum(i[1:])
  return 0

def min(i, mnn):
  if len(i) > 0:
    print(mnn)
    if mnn > i[0]:
      return min(i[1:], i[0])
    return min(i[1:], mnn)
  return mnn

def max(i, mxx):
  if len(i) > 0:
    print(mxx)
    if mxx < i[0]:
      return max(i[1:], i[0])
    return max(i[1:], mxx)
  return mxx

print(sum(i))
print()
print(min(i[1:], i[0]))
print()
print(max(i[1:], i[0]))
