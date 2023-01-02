'''
# My 1st Solution: O(n), but 734ms slow. 32.18% space complexity.
'''
def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
  match = 0
  checkIndex = -1
  
  if ruleKey == "type":
    checkIndex = 0
  elif ruleKey == "color":
    checkIndex = 1
  else:
    checkIndex = 2
  
  for item in items:
    if item[checkIndex] == ruleValue:
      match += 1
  
  return match

print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))
print(countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone"))

'''
# Found Solution: https://leetcode.com/problems/count-items-matching-a-rule/solutions/2891418/python-namedtuple/
  Modified to my approach. Faster at 515ms. Same time complexity and space complexity
import collections
def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
  colItem = collections.namedtuple('colItem', ['type', 'color', 'name'])
  matches = 0
  for item in items:
    if getattr(colItem(*item), ruleKey) == ruleValue:
      matches += 1
  
  return matches
'''

'''
# Found Solution: https://leetcode.com/problems/count-items-matching-a-rule/solutions/2891418/python-namedtuple/
  Ran it on my machine: 723ms but Space complexity 99.34% due to generators expression.
def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
  colItem = collections.namedtuple('colItem', ['type', 'color', 'name'])
  return sum(getattr(colItem(*item), ruleKey) == ruleValue for item in items)
'''