class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = "".join(char.lower() for char in s if char.isalnum())

        n = len(clean_string)

        for i in range(n // 2):
            if (clean_string[i] != clean_string[n-i-1]):
                return False

        return True
