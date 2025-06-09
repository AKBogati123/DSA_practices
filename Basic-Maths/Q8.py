"""
🧮 Question: Calculate Factorial

📄 Description:
Given a non-negative integer `n`, return the factorial of `n`.  
The factorial of a number n is the product of all positive integers less than or equal to n.  
Factorial is denoted as n!

📘 Example:
Input: n = 5  
Output: 120  
Explanation: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

class Solution:
    def factorial(self, n):
        if n == 0:
            return 1  # Base case: 0! = 1

        fact = 1  # Initialize factorial result

        for i in range(1, n + 1):
            fact *= i  # Multiply fact by i in each iteration

        return fact
