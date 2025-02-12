# Условие: Write a function that turn roman digits to integer.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Создаем словарь, где ключом являются латинские цифры,
        # а значением - арабские.
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        # Заготавливаем переменную под результат, который пока что равен нулю.
        answer = 0

        # Создаем цикл, который перебирает все индексы строки на входе.
        for i in range(len(s)):
            current_value = roman[s[i]]
            if i > 0 and roman[s[i - 1]] < current_value:
                answer += current_value - 2 * roman[s[i - 1]]
            else:
                answer += current_value

        return answer

# Примеры.
solution = Solution()
roman = 'XIV'
print(solution.romanToInt(roman))
