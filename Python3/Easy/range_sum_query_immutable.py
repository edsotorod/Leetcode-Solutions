class NumArray:

  def __init__(self, nums: list[int]):
    self.nums = nums
    self.acumilative = [0]
    
    for num in nums:
      self.acumilative.append(self.acumilative[-1] + num) 

  def sumRange(self, left: int, right: int) -> int:
    return self.acumilative[right] - self.acumilative[left]
    
    
'''
# Second Solution: Better Space Complexity
class NumArray:

  def __init__(self, nums: list[int]):
    self.nums = nums
    self.acumilative = [0]
    
    for num in nums:
      self.acumilative += [self.acumilative[-1] + num] 

  def sumRange(self, left: int, right: int) -> int:
    return self.acumilative[right + 1] - self.acumilative[left]
'''