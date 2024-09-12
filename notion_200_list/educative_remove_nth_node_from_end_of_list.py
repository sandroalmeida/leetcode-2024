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


def removeNthFromEnd(head, n):
    currentNode = head
    for i in range(n):
        currentNode = currentNode.next

    # edge case, if currentNode is null n = length of list
    # so the head need to be removed
    if currentNode is None:
        return head.next

    nodeBeforeRemove = head
    while currentNode.next is not None:
        currentNode = currentNode.next
        nodeBeforeRemove = nodeBeforeRemove.next

    nodeBeforeRemove.next = nodeBeforeRemove.next.next

    return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


result = removeNthFromEnd(head, 2)
if result is not None:
    result.print_list()


