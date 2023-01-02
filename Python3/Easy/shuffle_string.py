'''
# 2nd Solution: Found it in Solutions.
  Thought it was simple and clearly depicts what's being done.
  Learned about initializing "empty" list. Nice trick!
  Appearently slower and using more space than my initial solution.
  My thoughts:
  Creating a new list instead of using existing s to create the list.
'''
def restoreString(s: str, indices: list[int]) -> str:
  resStr = [''] * len(s)
  for i in range(len(s)):
    resStr[indices[i]] = s[i] 
    
  return "".join(resStr)

print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))
print(restoreString("abc", [0,1,2]))

'''
# 1st Solution: My messy solution, Faster and Better Space
def restoreString(s: str, indices: list[int]) -> str:
  s = list(s)
  size = len(s)
  index = 0
  while index < size:
    if index == indices[index]:
      index += 1
      continue
    else:
      temp = s[indices[index]]
      s[indices[index]] = s[index]
      s[index] = temp
      
      temp = indices[index]
      indices[index] = indices[temp]
      indices[temp] = temp    
    
  return "".join(s)
'''