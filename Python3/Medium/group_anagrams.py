'''
# 2nd Solution Attempt: https://leetcode.com/problems/group-anagrams/solutions/2750499/python-solution-using-counter-and-frozenset/?page=3
  This is where I learned of frozenset and defaultdict.
  On my machine: 397ms and 26.6 mb
'''
import collections
def groupAnagrams(strs: list[str]) -> list[list[str]]:
  anagramDict = collections.defaultdict(list)
  
  for str in strs:
    collCounter = collections.Counter(str).items()
    anagramDict[frozenset(collCounter)].append(str)

  return list(anagramDict.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))

'''
# 1st Attempt Solution: Exceeded Time Limit
  My idea was to make the counter a tuple, but was not aware
  that frozenset and defaultdict was a thing. Now I will rewrite it on top.
import collections
def groupAnagrams(strs: list[str]) -> list[list[str]]:
  counterDict = {}
  strDict = {}
  index = 0
  
  for str in strs:
    collCounter = collections.Counter(str)
    
    if collCounter not in counterDict.values():
      counterDict[index] = collCounter
      strDict[index] = [str]
      index += 1
    else:
      for key, value in counterDict.items():
        if value == collCounter:
          strDict[key].append(str)
  
  answer = []
  
  for val in strDict.values():
    answer.append(val)
  
  return answer
'''