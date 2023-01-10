# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

'''
1st Solution: Time Complexity O(2n) 37ms, Space Complexity O(1)
'''  
def getDecimalValue(head: ListNode) -> int:
  size = -1
  itr = head
  while itr:
    size += 1
    itr = itr.next

  total = 0
  itr = head
  while itr:
    total += itr.val * pow(2, size)
    size -= 1
    itr = itr.next

  return total

print(getDecimalValue([1,0,1]))
print(getDecimalValue([0]))

'''
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
# 2nd Solution: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/solutions/2813177/python-solution/
  Learned about int()
  Time Complexity O(2n) 28ms "int() binary conversion is O(n)", Space Complexity 0(n)    
class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    binary = ''
    itr = head
    while itr:
      if itr.val == 1:
        binary += '1'
      else:
        binary += '0'
      itr = itr.next
    
    return int(binary, 2)
'''