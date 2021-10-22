class Node:
    
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        
        curr = self.head
        i = 0
        
        while curr:
            if i == index:
                break
            curr = curr.next
            i += 1
            
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = Node(val)
            
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            
        self.size += 1
            

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = Node(val)
            
        else:
            new_node = Node(val)
            curr = self.head
            
            while curr.next:
                curr = curr.next
                
            curr.next = new_node
                
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return 
        
        new_node = Node(val)
        
        self.size += 1 
        
        if not self.head:
            self.head = new_node
            return 
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        curr = self.head
        i = 0
        
        while curr:
            if i == index - 1:
                break
            curr = curr.next
            i += 1
            
        new_node.next = curr.next
        curr.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return
        
        self.size -= 1
        
        if index == 0:
            self.head = self.head.next
            return
            
        curr = self.head
        i = 0
        
        while curr:
            
            if i == index - 1:
                break
            
            curr = curr.next
            i += 1
            
        curr.next = curr.next.next
                

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)