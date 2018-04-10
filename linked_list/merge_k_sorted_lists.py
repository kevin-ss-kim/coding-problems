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

l3.next = l5

l6.next = l8

l7.next = l10

def print_singly_linked_list(l):
    node = l
    while node:
        print str(node.val) + ' -> ',
        node = node.next
    print

def merge_two_sorted_lists(lists):
    nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    for x in sorted(nodes):
        point.next = ListNode(x)
        point = point.next
    print_singly_linked_list(head.next)

def main():
    merge_two_sorted_lists([l1, l3, l6, l7, l9])

main()