class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        c = 0
        result = []

        while i >= 0 or j >= 0 or c:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            total = bit_a + bit_b + c
            c = total // 2
            result.append(str(total % 2))

            i -= 1
            j -= 1

        return ''.join(result)[::-1]


class SolutionAlternative:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


sol = Solution()
print(sol.addBinary("1110", "10"))

sol = Solution1()
print(sol.addBinary("1110", "10"))
