class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sm = 0
        for i, v in zip(range(len(columnTitle)), columnTitle[::-1]):
            sm += (ord(v) - 64) * 26 ** i
        return sm


class Solution2(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for i in range(len(columnTitle)):
            result += (ord(columnTitle[~i]) - 64) * 26 ** i
        return result


print(Solution().titleToNumber('AABR'))
print(Solution2().titleToNumber('AABR'))
