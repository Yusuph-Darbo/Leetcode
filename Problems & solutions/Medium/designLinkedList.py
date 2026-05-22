class MyLinkedList(object):
    class ListNode:
        def __init__(self, val, next_node = None):
            self.val = val
            self.next = next_node

    def __init__(self):
        self.head = None
        self.length = 0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = self.ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = self.ListNode(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = newNode
        self.length += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.length:
            return

        if index <= 0:
            self.addAtHead(val)
            return

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        
        newNode = self.ListNode(val)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)