'''
# 1st Solution: Time complexity O(n logn), Space Complexity O(n). 297ms
'''
def sortPeople(names: list[str], heights: list[int]) -> list[str]:
  peopleHeights = {}
  
  for i in range(len(names)):
    peopleHeights[heights[i]] = names[i]
  
  heights.sort(reverse=True)
  
  for i in range(len(names)):
    names[i] = peopleHeights[heights[i]]
  
  return names

print(sortPeople(["Mary","John","Emma"], [180,165,170]))
print(sortPeople(["Alice","Bob","Bob"], [155,185,150]))

'''
# 2nd Solution: Learned about zi. 166ms
def sortPeople(names: list[str], heights: list[int]) -> list[str]:
  peopleHeights = dict(zip(heights,names))
  
  heights.sort(reverse=True)
  
  for i in range(len(names)):
    names[i] = peopleHeights[heights[i]]
  
  return names
'''