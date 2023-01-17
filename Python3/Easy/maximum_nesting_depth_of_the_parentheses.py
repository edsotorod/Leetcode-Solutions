'''
# 1st Solution: Time Complexity O(n) 28ms, Space Complexity O(1)
'''
def maxDepth(self, s: str) -> int:
  counter = 0
  maxDep = 0

  for index in s:
    if index is "(":
      counter += 1
      if counter > maxDep:
        maxDep = counter
    elif index is ")":
      counter -= 1
      
  return maxDep