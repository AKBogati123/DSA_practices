"""
🔎 Question: Find the Largest Digit in a Number

📄 Description:
Given an integer `n`, return the largest digit present in the number.

🔍 Example:
Input: n = 3792  
Output: 9  
Explanation: The digits are 3, 7, 9, 2. The largest digit is 9.
"""

class Solution:
    def largestDigit(self, n):
        large = 0  # Initialize largest digit to 0

        while n > 0:
            lastDigit = n % 10      # Extract the last digit
            if lastDigit > large:   # Update if current digit is greater
                large = lastDigit
            
            n = n // 10             # Remove the last digit
        
        return large
