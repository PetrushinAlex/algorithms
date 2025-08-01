# Написать функцию которая принимает список чисел, где каждый элемент
# встречается ровно 2 раза, кроме одного.

def solution(x: list[int]):
    for i in x:
        if x.count(i) == 1:
            return i


def solution2(x: list[int]):
    sumary = 0
    for i in x:
        sumary ^= i
    return sumary


a = [3, 3, 2, 2, 1]
b = [2, 2, 1]

print(solution2(a), solution2(b))

# возвращает элемент который встречается больше всех в списке

c = [1, 2, 1]
d = [1, 2, 1, 2, 1]
f = [1, 2, 4, 3, 4, 3, 4, 4, 4]


def solution3(x: list[int]):
    result = []
    for i in x:
        result.append((x.count(i), i))

    return max(result)[1]


print(solution3(c), solution3(f))
