# Given a singly linked list, delete the middle of the linked list. For example, if the given linked list is 1->2->3->4->5 then the linked list should be modified to 1->2->4->5

# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.

# If the input linked list is NULL, then it should remain NULL.

# If the input linked list has 1 node, then this node should be deleted and a new head should be returned.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# count nodes
def countOdNodes(head):
    current = head
    count = 0
    while current is not None:
        current = current.next
        count += 1
    return count


# Delete middle node and returns head of the modified list
def deleteMiddle(head, count):
    current = head
    currentIdx = 0
    midIdx = count // 2

    if (current == None):
        return None

    if (current.next == None):
        del current
        return None
    
    while current is not None:
        if (currentIdx == midIdx):
            break

        prev = current
        current = current.next
        currentIdx+=1
    
    prev.next = current.next

    return head


    

    

    


# Function to print the linked list
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
#f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
#e.next = f

print("Original Linked List:")
printLinkedList(a)

# Delete the middle node
count = countOdNodes(a) 
new_head = deleteMiddle(a, count)

print("Modified Linked List:")
printLinkedList(new_head)

print(Node(a))

