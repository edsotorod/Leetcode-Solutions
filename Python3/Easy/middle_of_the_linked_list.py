# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

'''
# 1st Solution: Time Complexity O(2n), Space Complexity O(1)
'''
def middleNode(head: None | ListNode) -> None | ListNode:
  count = 0
  itr = head

  while itr:
    count += 1
    itr = itr.next
  
  middle = count // 2
  itr = head
  count = 0

  while itr:
    if count == middle:
      return itr
    itr = itr.next
    count += 1
  
  return head

'''
# 2nd Solution: https://leetcode.com/problems/middle-of-the-linked-list/solutions/2879662/python-two-pointers-o-n/
  Have two pointers. The first pointer goes one at a time. The second pointer will always be double ahead the first pointer.
  When the second pointer reaches None, we return first.next for the remaining middle list.
'''