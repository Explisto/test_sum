def inverse_list(head: DLNode):

    current = head
    nx = None
    pr = None

    if head == None:
        return head

    while current:
        nx = current.next
        pr = current
        current.next = current.prev
        current.prev = pr

        current = nx

    return pr