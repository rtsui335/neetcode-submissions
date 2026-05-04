class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #brute force, going through each possible starting position
        #O(n * m) time complexity
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            j = 0
            while j < m:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
                if j == m:
                    return i

        return -1