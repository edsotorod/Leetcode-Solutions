'''
# 1st Solution: Slow, O(n) and O(n)
'''
def interpret(command: str) -> str:
  word = ""
  i = 0
  size = len(command)
  while i < size:
    if command[i] == "G":
      word += "G"
      i += 1
    elif command[i] == "(" and command[i+1] == ")":
      word += "o"
      i += 2
    else:
      word += "al"
      i += 4
  
  return word

print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))
print(interpret("(al)G(al)()()G"))