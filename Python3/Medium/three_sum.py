'''
# 2nd Solution: Time Complexity O(n^2) 1490ms, Space Complexity O(n)
# With help from https://leetcode.com/problems/3sum/solutions/3094404/best-solution-explained-with-animation-no-waste-of-time/
# - Only peeked at the optimal solution drawings
'''
def threeSum(nums: list[int]) -> list[list[int]]:
  nums.sort()
  size = len(nums)
  curr_num = 0
  solution = []
  
  while curr_num < (size - 2):
    if curr_num != 0:
      if nums[curr_num] == nums[curr_num - 1]:
        curr_num += 1
        continue
    
    left = curr_num + 1
    right = size - 1
    while left < right:
      total = nums[curr_num] + nums[left] + nums[right]
      if total < 0:
        left += 1
      elif total > 0:
        right -= 1
      else:
        solution.append([nums[curr_num], nums[left], nums[right]])
        left += 1
        right -= 1
        
        while nums[left] == nums[left - 1] and left < right:
          left += 1
        
        while nums[right] == nums[right + 1] and left < right:
          right -= 1
    
    curr_num += 1
  
  return solution

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print(threeSum([3,0,-2,-1,1,2]))
print(threeSum([-2,0,0,2,2]))

'''
# 1st Solution Attempt: Failed
# Did not take into account that all possible solutions
def threeSum(nums: list[int]) -> list[list[int]]:
  # step 1: sort the list of numbers
  nums.sort()
  
  # step 2: Create a dictionary of said numbers from the list
  numDict = {}
  for num in nums:
    if num not in numDict:
      numDict[num] = 1
    else:
      numDict[num] += 1
  
  unique3Sum = set()
  solution = []
  # step 3: iterate the sorted list, having two pointers add
  # Lookout 1: Potential use of a number twice when the list only has one copy
  # Lookout 2: 0 is the only number that can be used 3 times
  # - This only comes if the difference of the first two numbers and 0 is 0.
  for i in range(len(nums)- 1):
    index1 = nums[i]
    index2 = nums[i+1]
    twoSumDiff = 0 - (index1 + index2)
    
    numDict[index1] -= 1
    numDict[index2] -= 1
    
    if twoSumDiff in numDict:
      if numDict[twoSumDiff] > 0:
        temp = [index1, index2, twoSumDiff]
        temp.sort()
        temp = tuple(temp)
        if temp not in unique3Sum:
          unique3Sum.add(temp)
          solution.append([index1, index2, twoSumDiff])
          
    numDict[index1] += 1
    numDict[index2] += 1
  
  return solution
'''
