'''
# 2nd Solution: Using Stack to keep track, Same O(n) time complexity
'''
def balancedStringSplit(s: str) -> int:
  pairs = 0
  tracking = []
  
  for chr in s:
    if tracking == []:
      tracking.append(chr)
      pairs += 1
    elif chr == tracking[-1]:
      tracking.append(chr)
    else:
      tracking.pop()
  
  return pairs

print(balancedStringSplit("RLRRLLRLRL"))
print(balancedStringSplit("RLRRRLLRLL"))
print(balancedStringSplit("LLLLRRRR"))

'''
# 1st Solution: No stack use
def balancedStringSplit(s: str) -> int:
  pairs = 0
  startPair = 0
  count = 1
  index = 1
  size = len(s)

  while index < size:
    if s[startPair] == s[index]:
      count += 1
    elif s[startPair] != s[index]:
      count -= 1
    
    if count == 0:
      pairs += 1
      startPair = index + 1
      index += 1
      count = 1
    
    index += 1
  
  return pairs
'''

'''
Neat 3rd Solution: https://leetcode.com/problems/split-a-string-in-balanced-strings/solutions/2608029/python3/
'''