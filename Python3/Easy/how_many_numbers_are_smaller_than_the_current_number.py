def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
  numDict = {}
  solutionList = []
  
  for num in nums:
    if num not in numDict:
      numDict[num] = 0
    
  for num in nums:
    for key in numDict:
      if key > num:
        numDict[key] += 1
        
  for num in nums:
    solutionList.append(numDict[num])
  
  return solutionList

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([6,5,4,8]))
print(smallerNumbersThanCurrent([7,7,7,7]))
print(smallerNumbersThanCurrent([7]))
print(smallerNumbersThanCurrent([]))

'''
# Second Solution: Improved performance
def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
  solutionList = []
  sortList = sorted(nums)[:]

  for num in nums:
    solutionList.append(sortList.index(num))
  
  return solutionList
'''