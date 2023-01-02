'''
  # Not my solution: Looked it up online -> https://www.youtube.com/watch?v=OTMZe3vM3MI

  # Floyd's Algorithm: Turtle and Hare
'''
def findDuplicate(nums: list[int]) -> int:
  turtle = nums[0]
  hare = nums[0]

  turtle = nums[turtle]
  hare = nums[nums[hare]]

  # We are wanting an intersection
  while turtle != hare:
    turtle = nums[turtle]
    hare = nums[nums[hare]]

  turtle = nums[0]
  # Now we are looking for where they meet
  # when moving one node at a time
  while turtle != hare:
    turtle = nums[turtle]
    hare = nums[hare]
  
  return turtle

print(findDuplicate([3,1,3,4,2]))
print(findDuplicate([3,1,6,4,2,7,2,2,5]))
print(findDuplicate([2,2,2,2,2]))