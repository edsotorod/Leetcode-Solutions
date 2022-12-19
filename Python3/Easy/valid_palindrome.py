# First Solution: Using Regex
import re

def isPalindrome(s: str) -> bool:
  strLower = re.findall(r'[a-z0-9]', s.lower())
  
  left = 0
  right = len(strLower) - 1
  
  while (left < right):
    if strLower[left] != strLower[right]:
      return False
    
    left += 1
    right -= 1
  
  return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("race a car0"))
print(isPalindrome("0A man, a plan, a canal: Panama0"))
print(isPalindrome(" "))


'''
  # Second Solution with no Regex: Bad Time Complexity
  def isPalindrome(s: str) -> bool:
    newStr = s.lower()[:]
    for x in range(len(s)):
      if not s[x].isalnum():
        newStr = newStr.replace(s[x], "")
        
    
    left = 0
    right = len(newStr) - 1
    
    while (left < right):
      if newStr[left] != newStr[right]:
        return False
      
      left += 1
      right -= 1
    
    return True
'''