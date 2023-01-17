# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

'''
# 1st Solution: Time Complexity O(n) 68ms, Space Complexity O(1)
'''
def removeElements(head: None | ListNode, val: int) -> None | ListNode:
  if head:
    prevItr = head
    curItr = prevItr.next
    while curItr:
      if curItr.val is val:
        prevItr.next = curItr.next
        curItr = None
      else:
        prevItr = prevItr.next
      curItr = prevItr.next    
    
    if head.val is val:
      head = head.next
    
    return head
  else:
    return head