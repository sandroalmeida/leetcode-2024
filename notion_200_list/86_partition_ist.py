class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        current = self
        output = []
        while current:
            output.append(str(current.val))
            current = current.next
        print("->".join(output))

def partition(head, x):
    left, right = ListNode(), ListNode()
    lTail, rTail = left, right

    current = head
    while current:
        if current.val < x:
            lTail.next = current
            lTail = lTail.next
        else:
            rTail.next = current
            rTail = rTail.next
        current = current.next

    lTail.next = right.next
    rTail.next = None

    return left.next


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)


head.print_list()
new_list = partition(head, 3)
new_list.print_list()
