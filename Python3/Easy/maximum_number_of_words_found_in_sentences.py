def mostWordsFound(sentences: list[str]) -> int:
  maxFound = -1

  for sen in sentences:
    temp = sen.count(" ")
    if temp > maxFound:
      maxFound = temp

  return maxFound + 1

print(mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))
print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))
print(mostWordsFound(["please"]))
print(mostWordsFound([]))

'''
# 2nd Solution: Slow and O(n)
def mostWordsFound(sentences: list[str]) -> int:
  maxFound = 0
  
  for i in range(len(sentences)):
    sentences[i] = sentences[i].count(" ") + 1
    maxFound = max(maxFound, sentences[i])
  
  return maxFound
'''