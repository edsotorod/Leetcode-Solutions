class Node:
  def __init__(self, val=None, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insertAtFront(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.head.prev = node
      node.next = self.head
      self.head = node

  def print(self):
    itr = self.head
    strList = ''
    while itr:
      strList += ' <-- ' + str(itr.val) + ' --> '
      itr = itr.next
    print("Linked List:", strList)

  def moveToFront(self, node):
    # Case 1: Node at the end and has previous nodes
    if node.next is None and node.prev is not None:
      prev = node.prev
      prev.next = None
      self.tail = prev
      node.prev = None
      self.insertAtFront(node)
    # Case 2: Node is between nodes
    elif node.next is not None and node.prev is not None:
      prev = node.prev
      next = node.next
      prev.next = next
      next.prev = prev
      node.prev = None
      node.next = None
      self.insertAtFront(node)
  
  def removeTail(self):
    if self.tail.prev is None and self.tail.next is None:
      self.head = None
      del self.tail
      self.tail = None
    else:
      newTail = self.tail.prev
      newTail.next = None
      del self.tail
      self.tail = newTail

class LRUCache:
  def __init__(self, capacity: int):
    self.nodeDict = defaultdict(Node)
    self.linkList = LinkedList()
    self.maxCapacity = capacity
    self.curCapacity = 0

  def get(self, key: int) -> int:
    if key in self.nodeDict:
      if self.nodeDict[key].prev is not None:
        self.linkList.moveToFront(self.nodeDict[key])

      return self.nodeDict[key].val
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    if key in self.nodeDict:
      self.nodeDict[key].val = value
      self.linkList.moveToFront(self.nodeDict[key])
    else:
      node = Node(key, value, None, None)
      if self.curCapacity < self.maxCapacity:
        self.nodeDict[key] = node
        self.linkList.insertAtFront(node)
        self.curCapacity += 1
      else:
        del self.nodeDict[self.linkList.tail.key]
        self.linkList.removeTail()  
        self.linkList.insertAtFront(node)
        self.nodeDict[key] = node

    return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

