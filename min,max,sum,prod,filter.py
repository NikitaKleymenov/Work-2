import random

spisok = [random.randint(0, 100) for _ in range(15)]
spisok.sort()
x = 33

def minlist(massiv):
    return massiv[0]

def maxlist(massiv):
    return massiv[-1]

def sumlist(massiv):
    s = 0
    for i in massiv:
        if i != 0:
            s += i
    return s

def prodlist(massiv):
    m = massiv[0]
    for i in massiv:
        if i == 0:
            break
        m *= i
    return m

def filterlist(massiv, filtr):
    big, small = [], []
    for x in massiv:
        if x > filtr:
            big.append(x)
        elif x < filtr:
            small.append(x)
    print(f'Больше {filtr}: {big}, Меньше {filtr}: {small}')
    return big, small

print(f'Минимум: {minlist(spisok)}')
print(f'Максимум: {maxlist(spisok)}')
print(f'Сумма: {sumlist(spisok)}')
print(f'Произведение: {prodlist(spisok)}')
filterlist(spisok, x)
