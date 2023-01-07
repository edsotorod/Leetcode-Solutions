'''
# 1st Solution: Horrible. Time complexity O(n^2), Space Complexity O(n)
'''
def sortString(s: str) -> str:
  s = list(s)
  s.sort()
  
  msgOutput = ""
  index = -1
  
  while len(s) > 0:
    msgOutput += s[0]
    s.pop(0)
    index += 1
    
    for letter in s[:]:
      print(s, letter)
      if letter != msgOutput[index]:
        msgOutput += letter
        s.remove(letter)
        index += 1
    
    if len(s) == 0:
      break
    
    msgOutput += s[len(s) - 1]
    s.pop()
    index += 1
    
    for i in range(len(s)-1, -1, -1):
      if s[i] != msgOutput[index]:
        msgOutput += s[i]
        s.remove(s[i])
        index += 1   
  
  return msgOutput

print(sortString("aaaabbbbcccc"))
print(sortString("rat"))
print(sortString("leetcode"))

'''
# 2nd Solution: https://leetcode.com/problems/increasing-decreasing-string/solutions/531811/java-python-3-two-clean-codes-w-explanation-and-analysis/comments/468805
  Learned about collections.Counter and string.ascii_lowercase
import collections
import string
def sortString(s: str) -> str:
  counter, result = collections.Counter(s), []
  while counter:
    for traverse in string.ascii_lowercase, reversed(string.ascii_lowercase):
      result += [c for c in traverse if c in counter]
      counter -= dict.fromkeys(counter, 1)
  return ''.join(result)
  
'''