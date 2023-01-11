# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

'''
# 1st Solution: Time Complexity O(n) 43ms, Space Complexity O(n)
  Dummy is there to point at the beginning of the Linked List. 
  We ignore the initial node since it's not part of the lists being combined.
  Cur is being moved, so we can't return the entire merged list with it.
'''
def mergeTwoLists(list1: None | ListNode, list2: None | ListNode) -> None | ListNode:
  cur = dummy = ListNode()
  while list1 and list2:    
    if list1.val < list2.val:
      cur.next = list1
      cur = list1
      list1 = list1.next
    else:
      cur.next = list2
      cur = list2
      list2 = list2.next
          
  if list1 or list2:
    if list1:
      cur.next = list1
    else:
      cur.next = list2

  return dummy.next