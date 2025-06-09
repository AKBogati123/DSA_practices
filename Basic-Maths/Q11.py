"""
✅ Question: Check Prime Number

📄 Description:
A **Prime Number** is a number that has exactly two distinct positive divisors: 1 and itself.

📘 Example:
Input: n = 7  
Output: True  
Explanation: 7 is divisible only by 1 and 7, so it is a prime number.
"""

class Solution:
    def isPrime(self, n):
        count = 0

        # Count the number of divisors
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        # A number is prime if it has exactly two divisors: 1 and itself
        return count == 2
