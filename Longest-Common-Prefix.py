class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        minimum_length = 300
        for i in strs:
            length = len(i)
            if length<minimum_length:
                minimum_length = length
        for i in range(minimum_length):
            for j in strs:
                if j[i] != strs[0][i]:
                    return ans
            ans = ans + strs[0][i]
        return ans
