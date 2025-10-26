'''
Common Python List Operation Costs:
    Accessing an element by index (e.g., my_list[i]): O(1) - Constant time. This is because Python lists are implemented as dynamic arrays, allowing direct access to any element via its memory address.
    Appending an element to the end (e.g., my_list.append(item)): O(1) amortized. While occasional reallocations might lead to a temporary O(N) cost, the average cost over many appends remains constant.
    Popping an element from the end (e.g., my_list.pop()): O(1) - Constant time.
    Getting the length of the list (e.g., len(my_list)): O(1) - Constant time.
    Inserting an element at the beginning or middle (e.g., my_list.insert(0, item) or my_list.insert(N/2, item)): O(N) - Linear time. This requires shifting subsequent elements to accommodate the new item.
    Deleting an element at the beginning or middle (e.g., del my_list[0] or my_list.pop(N/2)): O(N) - Linear time. Similar to insertion, this requires shifting elements.
    Searching for an element (e.g., item in my_list): O(N) - Linear time in the worst case, as it may require iterating through the entire list.
    Slicing a list (e.g., my_list[x:y]): O(k), where k is the length of the slice. This involves creating a new list.
    Sorting a list (e.g., my_list.sort() or sorted(my_list)): O(N log N) - Log-linear time. Python's Timsort algorithm is efficient for various data distributions.
    Reversing a list (e.g., my_list.reverse()): O(N) - Linear time, as each element's position needs to be changed.
    Concatenating lists (e.g., list1 + list2): O(k), where k is the length of the second list. This creates a new list.
    Multiplying a list (e.g., my_list * n): O(N*k) where N is the original list length and k is the multiplier. This creates a new list with repeated elements.
'''
'''
class Node:
    def __init__(self, next):
        self.data = self
        self.next = None

    def printList(self):
        cur = self
        while cur != None:
            print(cur.data, end=' ')
            cur = cur.next
        print("")

    def insertAfter(self, node):
        temp = self.next
        self.next = node
        node.next = temp

    def insertAtEnd(self, node):
        cur = self
        while cur.next != None:
            cur = cur.next
        cur.insertAfter(node)


head = Node("A")
head.insertAfter(Node("B"))
'''

'''
class Node:
    def __init__(self, d, n):
        self.data = d
        self.next = n

    def printList(self):
        cur = self
        while cur != None:
            print(cur.data, end=' ')
            cur = cur.next
        print("")
    
head = Node("A", Node("B", Node("C", None)))
head.printList()
'''
