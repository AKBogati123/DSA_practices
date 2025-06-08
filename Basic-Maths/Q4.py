"""
🔁 Question: Reverse a Number

📄 Description:
Given an integer `n`, return its reverse. The reverse should ignore the sign 
(i.e., treat negative numbers as positive) and return the reversed digits.

🔍 Example:
Input: n = 1234  
Output: 4321  
Explanation: Reversing the digits of 1234 gives 4321.
"""

class Solution:
    def reverseNumber(self, n):
        # Step 1: Take the absolute value to ignore any negative sign
        n = abs(n)

        # Step 2: If the number is 0, return 0 immediately
        if n == 0:
            return 0

        reverse = 0  # This will store the reversed number

        # Step 3: Loop until the number becomes 0
        while n > 0:
            a = n % 10              # Get the last digit
            reverse = reverse * 10 + a  # Append it to the reverse number
            n = n // 10             # Remove the last digit from the original number

        # Step 4: Return the reversed number
        return reverse
