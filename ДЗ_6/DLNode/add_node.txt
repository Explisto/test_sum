def add_node(head: DLNode, nodenum: int):

    current = head
    count = 0
    bf = DLNode(nodenum)
    nx = None

    if head == None:
        head = bf
        return head

    if nodenum < 0:
        return head

    if nodenum == 0:
        bf_head = head
        head = bf
        head.next = bf_head
        head.prev = None
        return head

    if head.next == None:
        if nodenum == 2:
            head.next = bf
            return head

    while current and current.next:

        if count + 1 == nodenum:
            nx = current.next
            current.next = bf
            current.next.prev = current
            current = current.next
            current.next = nx
            current.next.prev = current

        count += 1
        current = current.next

    if (count + 1 == nodenum):
        current.next = bf
        current.next.prev = current
        bf.next = None
        current = current.next

    return head