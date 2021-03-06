class Solution(object):
    def kmp(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        prefix = self.get_prefix(needle)
        i, j, length_haystack, length_needle = 0, 0, len(haystack), len(needle)

        while i < length_haystack and j < length_needle:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = prefix[j]

        if j == length_needle:
            return i - j
        else:
            return -1

    @staticmethod
    def get_prefix(needle):
        k, j, prefix = -1, 0, [-1] * len(needle)
        while j < len(needle) - 1:
            if k == -1 or needle[k] == needle[j]:
                k += 1
                j += 1
                if needle[k] != needle[j]:
                    prefix[j] = k
                else:
                    prefix[j] = prefix[k]
            else:
                k = prefix[k]

        return prefix
