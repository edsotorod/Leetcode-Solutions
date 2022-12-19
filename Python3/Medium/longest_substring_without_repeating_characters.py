def lengthOfLongestSubstring(s: str) -> int:
  dict = {}
  
  start = 0
  max = 0
  size = len(s)
  for index in range(size):
    if s[index] not in dict:
      dict[s[index]] = index
    else:
      if dict[s[index]] < start:
        dict[s[index]] = index
        continue
      currMax = (index - start)
      if max < currMax:
        max = currMax
      start = dict[s[index]] + 1
      dict[s[index]] = index
  
  if max < (size - start):
    max = size - start
      
  return max

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("pwker"))
print(lengthOfLongestSubstring("tmmzuxt"))
print(lengthOfLongestSubstring(""))