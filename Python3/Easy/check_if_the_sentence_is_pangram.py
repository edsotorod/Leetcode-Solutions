def checkIfPangram(sentence: str) -> bool:
  charSet = set()

  for letter in sentence:
    charSet.add(letter)

  return len(charSet) == 26

print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(checkIfPangram("leetcode"))

'''
# Second Solution: Faster and O(1) space
def checkIfPangram(sentence: str) -> bool:
  return len(set(sentence)) == 26
'''