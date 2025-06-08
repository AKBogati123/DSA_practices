"""
🧠 Question: Count the Number of Digits in an Integer

Description:
Given an integer `n`, return the number of digits in the number.

Note:
- The number may be negative.
- The number 0 has exactly 1 digit.

Example:
Input: n = 14  
Output: 2
"""

class Solution:
    def countDigit(self, n):
        if n == 0:
            return 1

        n = abs(n)
        count = 0

        while n > 0:
            n = n // 10
            count += 1

        return count
