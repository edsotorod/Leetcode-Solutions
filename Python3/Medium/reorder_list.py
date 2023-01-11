# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
# 1st Solution: Time Complexity O(n + n/2) 101ms, Space Complexity O(n)
'''
def reorderList(head: None | ListNode) -> None:
    """
      Do not return anything, modify head in-place instead.
    """
    nodeDict = {}
    count = 0
    itr = head

    while itr:
      nodeDict[count] = itr
      count += 1
      itr = itr.next

    if count == 2:
      return

    itr = head
    if count > 2:
      itr.next = nodeDict[count-1]
      itr = itr.next

    count -= 1
    index = 1

    while index < count:
      itr.next = nodeDict[index]
      index += 1
      itr = itr.next
      itr.next = nodeDict[count-1]
      count -= 1
      itr = itr.next

    itr.next = None