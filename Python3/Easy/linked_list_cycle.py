# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

'''
1st Solution: Time Complexity O(n) 54ms, Space Complexity O(n)
'''
import collections
def hasCycle(head: None | ListNode) -> bool:
  linkedDict = collections.defaultdict(ListNode)
  itr = head
  
  while itr:
    if itr in linkedDict:
      return True
    else:
      linkedDict[itr] = ''
    itr = itr.next

  return False

'''
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


# 2nd Solution: Use two pointers to keep track
  Time Complexity O(n) 56ms, Space Complexity O(1)
def hasCycle(head: None | ListNode) -> bool:
  if not head:
    return False
  
  itrCurr = head
  itrAhead = head.next
  while itrCurr != itrAhead:
    if itrAhead == None or itrAhead.next == None:
      return False
    itrCurr = itrCurr.next
    itrAhead = itrAhead.next.next

  return True
'''