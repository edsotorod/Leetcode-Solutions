'''
# 1st Solution: Time Complexity O(n) 32ms, Space Complexity O(n)
'''
def removeOuterParentheses(self, s: str) -> str:
  startIndex = 0
  endIndex = 0
  counter = 0
  solution = ""

  for index in s:
    if index is "(":
      counter += 1
    else:
      counter -= 1
    endIndex += 1
    
    if counter is 0:
      solution += s[startIndex+1:endIndex-1]
      startIndex = endIndex
  
  return solution