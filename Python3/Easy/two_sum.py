'''
  # Complexity: n logn + n
'''
def two_sum(nums: list[int], target: int) -> list[int]:
  numSort = nums[:]
  numSort.sort()
  size = len(nums)
  right = 0
  left = size - 1
  
  while True:
    if numSort[right] + numSort[left] > target:
      left -= 1
    elif numSort[right] + numSort[left] < target:
      right += 1
    else:
      right = numSort[right]
      left = numSort[left]
      break

  target1 = -1
  target2 = -1
  for x in range(size):
    if nums[x] == right and target1 == -1:
      target1 = x
      continue
    elif nums[x] == left and target2 == -1:
      target2 = x
      continue
    elif target1 != -1 and target2 != -1:
      break
    
  return [target1, target2]

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))

# ---------------------------------

'''
# Old Solution: Better time wise
def twoSum(self, nums: List[int], target: int) -> List[int]:
  dict = {}
  start = 0
  while start < len(nums):
      curr_num = nums[start]
      target_remainder = target - curr_num
      if curr_num in dict:
        return [dict[curr_num], start]
      dict[target_remainder] = start
      start += 1
'''