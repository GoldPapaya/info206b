
# Sentinel is just a way of specifying the start of the DLL.

# DLL with Sentinel
class Node:
    def __init__(self,data):
        self.data = data
        self.next = self # self referential (not None)
        self.prev = self #

    def insert_after(self, data):
        x = self
        y = Node(data)   # make a new Node object.
        z = x.next       # y goes between x and z
        y.prev = x
        y.next = z
        x.next = y
        z.prev = y
        
    def print_all(self):
        n = self.next # skip over sentinel
        while( n.data != None ):
            print(n.data, end=" - " )
            n = n.next
        print("")

head = Node(None)
head.insert_after("1")
head.insert_after("3")
head.insert_after("2")
head.insert_after("1")
head.insert_after("0")
head.print_all()

# x.prev.next = x.next
# y.next.prev = x.prev

'''
Linked Lists
insert: O(1)
append: O(1)
delete: O(1)
find: O(n)
access: O(n)

Lists
insert: O(n)
append: O(1), sometimes O(n)
delete: O(n)
find: O(n)
access: O(1)
'''

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def insert(self, node):
        cur = self
        while cur.data > node.data:
            cur = cur.next
        temp = cur.next
        cur.next = node
        node.next = temp
    
    def printList(self):
        cur = self
        while cur != None:
            print(cur.data, end=' ')
            cur = cur.next
        print("")

head = Node(1)
head.insert(Node(2))
head.insert(Node(3))
print(head.printList())
'''