# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# 
# Example 1:
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
# 
# Input: "race a car"
# Output: false
import re
class Solution:
        def isPalindrome(self, s: 'str') -> 'bool':
                  s = s.lower()
                  s = re.sub(r'\W+', '', s)
                  print("Al derecho: ",s)
                  s2 = s[::-1]
                  print("Al revés: ",s2)

                  if s == s2:
                          return True
                  return False




                  
p = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(p)

