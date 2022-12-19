def containsDuplicate(nums: list[int]) -> bool:
  dict = {}
  
  for n in nums:
    if n in dict:
      return True
    else:
      dict[n] = ""
  
  return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

'''
 # New Solution: After submitting the above
def containsDuplicate(nums: list[int]) -> bool:
  return len(nums) != len(set(nums))
'''