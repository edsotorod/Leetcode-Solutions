# Definition for singly-linked list.
class ListNode:
  def __init__(self, x, next=None):
    self.val = x
    self.next = next

'''
# Not a Working Solution: My attempt using a Linked List.
  Exceeds time limit.
  Solution found online: https://leetcode.com/problems/design-hashset/solutions/1970760/java-python-basic-hashtable-implementation/?page=2
'''
class MyHashSet:

  def __init__(self):
    self.head = None

  def add(self, key: int) -> None:
    if self.head == None:
      self.head = ListNode(key, self.head)
    
    if not self.contains(key):
      itr = self.head

      while itr:
        if itr.next == None:
          itr.next = ListNode(key)
          break
        itr = itr.next
    
    return

  def remove(self, key: int) -> None:
    if self.head == None:
      return
        
    itr = self.head
    
    if itr.val == key:
      self.head = itr.next
      self.print()
      return

    while itr:
      if itr.next != None:
        if itr.next.val == key:
          itr.next = itr.next.next
          break
      itr = itr.next
    self.print()
    return
    

  def contains(self, key: int) -> bool:
    itr = self.head
    while itr:
      if itr.val == key:
        return True
      itr = itr.next
    
    return False
      
  def print(self):
    itr = self.head
    linkList = ''
    while itr:
      linkList += str(itr.val) + ' --> '
      itr = itr.next
    print(linkList)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)