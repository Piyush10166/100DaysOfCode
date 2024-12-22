class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_str = ""
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        strs.sort()
        last = min(len(strs[0]), len(strs[-1]))
        j = 0
        while j < last and (strs[0][j] == strs[len(strs)-1][j]):
            new_str += strs[0][j]
            j += 1
        return new_str