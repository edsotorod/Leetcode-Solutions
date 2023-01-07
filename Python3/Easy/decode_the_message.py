'''
# 1st Solution: Time complexity O(n), Space Complexity O(n)
'''
def decodeMessage(key: str, message: str) -> str:
  letterDict = {}
  lwrCaseChar = 97
  
  for letter in key:
    if letter not in letterDict and letter != " ":
      letterDict[letter] = chr(lwrCaseChar)
      lwrCaseChar += 1
  
  decodeMsg = ""
  
  for letter in message:
    if letter == " ":
      decodeMsg += " "
    else:
      decodeMsg += letterDict[letter]
  
  return decodeMsg

print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
print(decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))