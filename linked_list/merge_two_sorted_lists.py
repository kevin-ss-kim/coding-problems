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
l2.next = l4
l4.next = l9

l3.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l10

def print_singly_linked_list(l):
    node = l
    while node:
        print str(node.val) + ' -> ',
        node = node.next
    print

def merge_two_sorted_lists(l1, l2):
    head = None
    if l1 is None:
        head = l2
    elif l2 is None:
        head = l1
    else:
        # Begin iterating
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        pointer = head
        while l1 and l2:
            if l1.val > l2.val:
                pointer.next = l2
                l2 = l2.next
            else:
                pointer.next = l1
                l1 = l1.next
            pointer = pointer.next
        pointer.next = l1 if l1 is not None else l2
    print_singly_linked_list(head)

def main():
    merge_two_sorted_lists(l1, l3)

main()