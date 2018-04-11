# Merge two sorted singly-linked lists that returns a merged sorted list that are made up elements of the two singly-linked list

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)
l9 = ListNode(9)
l10 = ListNode(10)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9
l9.next = l10

def has_cycle(l):
    if l is None:
        return False
    slow = fast = l
    while True:
        slow = slow.next
        if fast.next != None:
            fast = fast.next.next
        else:
            return False
        if (slow is None) or (fast is None):
            return False
        if slow == fast:
            return True

def main():
    print(has_cycle([l1, l3, l6, l7, l9]))

main()