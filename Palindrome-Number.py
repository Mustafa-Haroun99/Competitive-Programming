class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        length = len(string)
        for i in range(length // 2):
            if string[i] != string[-(i + 1)]:
                return False
        return True
        
