import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        odd_char = ""
        half_counts = {}
        
       
        for char, count in counts.items():
            if count % 2 != 0:
                odd_char = char
            if count // 2 > 0:
                half_counts[char] = count // 2
                
        m = sum(half_counts.values())
        
        
        current_ways = math.factorial(m)
        for count in half_counts.values():
            current_ways //= math.factorial(count)
            
        
        if k > current_ways:
            return ""
            
        first_half = []
        chars = sorted(half_counts.keys())
        
        
        for i in range(m):
            for char in chars:
                if half_counts[char] > 0:
                   
                    ways = current_ways * half_counts[char] // (m - i)
                    
                    if k <= ways:
                     
                        first_half.append(char)
                        half_counts[char] -= 1
                        current_ways = ways
                        break
                    else:
                       
                        k -= ways
                        
        res = "".join(first_half)
       
        return res + odd_char + res[::-1]