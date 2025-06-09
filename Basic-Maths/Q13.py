"""
✅ Question: Count Prime Numbers up to N

📄 Description:
Given a number `n`, count how many prime numbers are there from `1` to `n` (inclusive).
A **prime number** is a number greater than 1 that has exactly two positive divisors: 1 and itself.

📘 Example:
Input: n = 10  
Output: 4  
Explanation: Prime numbers from 1 to 10 are [2, 3, 5, 7] → total = 4
"""

class Solution:
    def primeUptoN(self, n):
        total = 0

        # Check each number from 1 to n
        for i in range(1, n + 1):
            count = 0

            # Count divisors of i
            for j in range(1, i + 1):  # ✅ Fix: inner loop should run till i, not n
                if i % j == 0:
                    count += 1

            # If exactly 2 divisors → prime
            if count == 2:
                total += 1

        return total
