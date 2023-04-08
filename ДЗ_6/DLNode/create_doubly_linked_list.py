def create_doubly_linked_list(numbers: list):
    head = None
    tail = None
    current = head

    if len(numbers) != 0:

        current = DLNode(numbers[0])
        head = current

        for item in range(1, len(numbers)):

            new_node = DLNode(numbers[item])
            current.next = new_node
            new_node.prev = current
            current = current.next

        tail = current

    return head