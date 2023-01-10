# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
'''
1st Solution: Time Complexity O(2n) 46ms, Space Complexity O(n)
'''
def reverseList(head: None | ListNode) -> None | ListNode:
  revList = []

  itr = head
  while itr:
    revList.append(itr.val)
    itr = itr.next
  
  itr = head
  size = len(revList) - 1
  while itr:
    itr.val = revList[size]
    size -= 1
    itr = itr.next
  
  return head
  
'''
# 2nd Solution: https://leetcode.com/problems/reverse-linked-list/solutions/3011853/python-solution-with-step-by-step-video/
  Neat solution that only iterates once
  Time Complexity O(n) 34ms, Space Complexity O(n)
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def reverseList(head: None | ListNode) -> None | ListNode:
  revList = None
  itr = head
  
  while itr:
    nextNode = itr.next
    itr.next = revList
    revList = itr
    itr = nextNode
  
  return revList
'''