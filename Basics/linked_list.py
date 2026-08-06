class Node:
    def __init__(self, value):
        self.value = value   # instance attribute — this node's data
        self.next = None     # instance attribute — pointer to the next node
        self.prev = None
        

class LinkedList:
    def __init__(self):
        self.head = None    # points to the first node in the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
        
    def search(self, value):
        current = self.head
        while current is not None:
            if(current.value == value):
                return True
            current = current.next
        return False
    
    def sum_list(self):
        total = 0
        current = self.head
        while current is not None:
            total += current.value
            current = current.next
        return total
        
    def print_reverse(self):
        self.helper(self.head)
    def helper(self,node):
        if(node is None):
            return
        self.helper(node.next)
        print(node.value, end=" ")
        
    
    def reverse(self):
        current = self.head
        previous = None
        
        while current is not None:
            
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        self.head = previous    
    
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value
        
    
    
    
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
# ll.print_list()
# print(ll.length())
# print(ll.search(99))
# print(ll.sum_list())
# ll.print_reverse()
ll.reverse()
print(ll.find_middle())
