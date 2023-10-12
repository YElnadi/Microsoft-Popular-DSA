class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):

        s = set()
        current = headA
        while current is not None:
            s.add(current)
            current = current.next

        current = headB
        while current is not None:
            if current in s:
                return current
            current = current.next

        return None


# Function to print the linked list
# def printLinkedList(head):
#     current = head
#     while current is not None:
#         print(current.val, end=" -> ")
#         current = current.next
#     print("None")
a = ListNode(4)
b = ListNode(1)
c = ListNode(8)
d = ListNode(4)
e = ListNode(5)


a.next = b
b.next = c
c.next = d
d.next = e


x = ListNode(5)
y = ListNode(6)
z = ListNode(1)
k = ListNode(8)
l = ListNode(4)
m = ListNode(5)

x.next = y
y.next = z
z.next = k
k.next = l
l.next = m

# Now, let's find the intersection node
solution = Solution()
intersection_node = solution.getIntersectionNode(a, x)

if intersection_node is not None:
    print("Intersection node value:", intersection_node.val)
else:
    print("No intersection found")
