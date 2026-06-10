class Solution(object):
    def isPalindrome(self, x):
        # Negative number palindrome nahi hota
        # Aur 10, 100 jaise ending 0 wale bhi nahi
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Even digits: x == reversed_half
        # Odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
