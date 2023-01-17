'''
# 1st Solution: Time Complexity O(n) 27ms, Space Complexity O(n)
'''
def isValid(self, s: str) -> bool:
  stack = []

  paren_dict = {
    "}": "{",
    "]": "[",
    ")": "("
  }
  
  for index in s:
    if index in paren_dict:
      if len(stack) is 0:
        return False
      else:
        if stack.pop() is not paren_dict[index]:
          return False
    else:
      stack.append(index)
  
  return len(stack) is 0