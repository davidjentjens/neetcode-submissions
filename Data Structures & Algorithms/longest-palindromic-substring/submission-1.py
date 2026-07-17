class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def getOddPalindromeFrom(index: int) -> str:
            left, right = index, index
            while left-1 >= 0 and right+1 < n and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            return s[left: right+1]

        def getEvenPalindromeFrom(left: int, right: int) -> str:
            if s[left] != s[right]:
                return ''
            while left-1 >= 0 and right+1 < n and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            return s[left: right+1]

        largest_palindrome = ''

        for i in range(n):
            even_palindrome = getOddPalindromeFrom(i)
            if len(even_palindrome) > len(largest_palindrome):
                largest_palindrome = even_palindrome

            if i+1 < n:
                odd_palindrome = getEvenPalindromeFrom(i, i+1)
                if len(odd_palindrome) > len(largest_palindrome):
                    largest_palindrome = odd_palindrome
            

        return largest_palindrome
