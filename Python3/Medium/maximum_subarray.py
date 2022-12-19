import sys
'''
 # Not my solution. Could not figure it out on my own.
 # Looked up Kadane's Algorithm
'''
def maxSubArray(nums: list[int]) -> int:
  max = -sys.maxsize
  curr = 0
  
  for n in nums:
    curr += n
    if curr > max:
      max = curr
    if curr < 0:
      curr = 0
  
  return max

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))