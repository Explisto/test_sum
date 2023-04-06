def remove_node(head: DLNode, nodenum: int):

    current = head
    bf = None
    count = 0

    if head == None:
        return None

    if head.next == None:
        if nodenum == 1:
            return None
        else:
            return head

    if nodenum < 0:
        return head

    if nodenum == 0:
        head = head.next
        head.prev = None
        return head

    while current and current.next:

        if count + 1 == nodenum:
            if current.next.next:
                current.next = current.next.next
                current.next.prev = current
                current = current.next
            else:
                current.next = None
                # current.next.prev = current
        else:
            current = current.next

        count += 1


    return head