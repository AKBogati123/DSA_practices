"""
🔁 Question: Check if a Number is a Palindrome

📄 Description:
Given an integer `n`, check whether it is a palindrome.
A number is said to be a palindrome if it reads the same backward as forward.

🔍 Example:
Input: n = 121  
Output: True  
Explanation: Reversing 121 gives 121, which is the same as the original number.
"""

class Solution:
    def isPalindrome(self, n):
        temp = n        # Store the original number for comparison
        rev = 0         # This will store the reversed number

        if n == 1:
            return True  # A single-digit number is always a palindrome

        while n > 0:
            num = n % 10            # Extract the last digit
            rev = rev * 10 + num    # Build the reversed number
            n = n // 10             # Remove the last digit

        # Compare the reversed number with the original
        return temp == rev
