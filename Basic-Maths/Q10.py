"""
✅ Question: Check Perfect Number

📄 Description:
A **Perfect Number** is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).
For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, 14 and 1+2+4+7+14 = 28.

📘 Example:
Input: n = 28  
Output: True  
Explanation: 1 + 2 + 4 + 7 + 14 = 28
"""

class Solution:
    def isPerfect(self, n):
        num = n
        sums = 0

        # Find all proper divisors of n and sum them
        for i in range(1, n):
            if n % i == 0:
                sums += i

        # Return True if the sum of divisors equals the original number
        return sums == num
