"""
🔎 Question: Find All Divisors of a Number

📄 Description:
Given an integer `n`, return a list of all its divisors.

🔍 Example:
Input: n = 12  
Output: [1, 2, 3, 4, 6, 12]  
Explanation: All numbers that divide 12 exactly without leaving a remainder are its divisors.
"""

class Solution:
    def divisors(self, n):
        ans = []  # List to store all divisors

        for i in range(1, n + 1):
            if n % i == 0:
                ans.append(i)  # If i divides n, add it to the list
            
        return ans
