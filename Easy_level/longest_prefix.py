# Условие: Write a function to find the longest
# common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Сразу отсекаем случай с пустым массивом.
        if not strs:
            return ''

        # Первое слово из списка будет префиксом.
        prefix = strs[0]

        # Перебираем остальные слова.
        for word in strs[1:]:
            # С помощью метода startswith проверяем,
            # начинается ли строка с текущего префикса.
            while not word.startswith(prefix) and prefix:
                # Уменьшаем префикс на 1 символ до тех пор,
                # пока префикс не совпадет.
                prefix = prefix[:-1]

        return prefix


# Примеры.
solution = Solution()
strs = ['motel', 'moonlight', 'motocycle']
print(solution.longestCommonPrefix(strs))
strs = []
print(solution.longestCommonPrefix(strs))
strs = ['God', 'Goddes', 'Goddamn']
print(solution.longestCommonPrefix(strs))
