"""
🔢 Question: Check Armstrong Number

📄 Description:
An **Armstrong number** is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
For example, 153 is an Armstrong number because 1³ + 5³ + 3³ = 153.

📘 Example:
Input: n = 153  
Output: True  
Explanation: 1³ + 5³ + 3³ = 153, so it is an Armstrong number.
"""

class Solution:
    def isArmstrong(self, n):
        power = 0                # To count the number of digits
        temp = n
        sum_digit = 0

        # Count number of digits in the number
        while temp > 0:
            power += 1
            temp = temp // 10

        num = n  # Store original number for processing

        # Compute the sum of digits raised to the power
        while num > 0:
            a = num % 10
            sum_digit += a ** power
            num = num // 10

        # Check if sum equals original number
        return sum_digit == n
