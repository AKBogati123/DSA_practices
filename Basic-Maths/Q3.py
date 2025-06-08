"""
🧠 Question: Count Odd Digits in an Integer

Description:
Given an integer `n`, return the count of digits in `n` that are odd numbers.

Notes:
- The input number may be negative.
- Ignore the sign of the number.
- The digit 0 is not considered odd.

Example:
Input: n = 12345  
Output: 3  
Explanation: The odd digits are 1, 3, and 5.
"""

class Solution:
    def countOddDigit(self, n):
        if n == 0:
            return 0

        n = abs(n)
        odd_count = 0

        while n > 0:
            digit = n % 10
            if digit % 2 != 0:
                odd_count += 1
            n = n // 10

        return odd_count
