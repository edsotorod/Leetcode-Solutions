'''
# Second Solution: Better Time Complexity -> O(n)
'''
def isAnagram(s: str, t: str) -> bool:
  dict = {}
  
  if (len(s) != len(t)):
    return False
  
  for x in range(len(s)):
    if s[x] not in dict:
      dict[s[x]] = 1
    else:
      dict[s[x]] += 1
    if t[x] not in dict:
      dict[t[x]] = -1
    else:
      dict[t[x]] -= 1
  
  for d in dict.values():
    if d != 0:
      return False
  
  return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))

'''
 # First Solution: Time Complexity -> O(nlogn)
def isAnagram(s: str, t: str) -> bool:
  return sorted(s) == sorted(t)
'''