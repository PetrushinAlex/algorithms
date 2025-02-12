# Условие: Given an integer x, return true if x is a
# palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Учитываем вариант с отрицательным числом на входе.
        # Он всегда возвращает false.
        if x < 0:
            return False
        # С помощью list comprehension собираем
        # список из цифр числа на входе.
        num_list = [int(digit) for digit in str(x)]
        # Проверяем на равенство получившийся массив
        # с этим же списком наоборот.
        if num_list == num_list[::-1]:
            return True
        return False


# Примеры.
solution = Solution()
num = 232
print(solution.isPalindrome(num))
num = 445
print(solution.isPalindrome(num))
num = 123454321
print(solution.isPalindrome(num))
