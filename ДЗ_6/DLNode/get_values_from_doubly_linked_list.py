def get_values_from_doubly_linked_list(head: DLNode):

    list_ = []
    current = head

    if head == None:
        return list_

    while current:
        list_.append(current.val)
        current = current.next

    print(list_)
    return list_
