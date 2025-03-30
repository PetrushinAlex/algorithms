# Условие: на вход получен массив чисел определенной длины (диапазон [0, n]).
# Необходимо вернуть пропущенное число.

class Solution:
    def missing_digit(self, nums: list[int]) -> int:
        n = len(nums)
        # Расчитываем ожидаемую сумму чисел от 0 до n;
        # Она равна n * (n + 1) / 2 (формула суммы арифметической прогрессии).
        expected = (n * (n + 1)) // 2
        # Актуальная сумма чисел массива nums - это просто расчет с помощью функции sum.
        actual = sum(nums)
        # Как результат - разница между ожидаемым и актуальным и есть наше число.
        return expected - actual


# Примеры
solution = Solution()

print(solution.missing_digit([0, 3, 1, 5, 2]))
print(solution.missing_digit([0, 1, 5, 3, 4, 6]))
print(solution.missing_digit([4, 1, 2, 3]))