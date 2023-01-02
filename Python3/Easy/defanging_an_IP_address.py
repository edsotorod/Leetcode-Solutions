import re
def defangIPaddr(address: str) -> str:
  return re.sub(r'[.]', '[.]', address)

print(defangIPaddr("1.1.1.1"))
print(defangIPaddr("255.100.50.0"))

'''
# 1st Solution: Slow and O(n*3)
def defangIPaddr(address: str) -> str:
  return address.replace(".", "[.]")
'''