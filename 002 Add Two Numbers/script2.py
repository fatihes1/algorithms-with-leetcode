# Function params => l1: Optional[ListNode], l2: Optional[ListNode]
# Data type that the function returns => Optional[ListNode]

def addTwoNumbers(l1, l2):
    # head of the new linked list (summary linked list)
    head = None
    # Reference of head
    temp = None
    # Carry
    carry = 0

    while l1 is not None or l2 is not None:
        # Each iteration we have to add carry from the last iteration
        sum = carry

        # Linked list lengths may be unequal so we are checking if the current node still in list or not
        if l1 is not None:
            sum = sum + l1.val
            l1 = l1.next
        if l2 is not None:
            sum = sum + l2.val
            l2 = l2.next
        # Add the total sum % 10 to new node
        node = ListNode(sum % 10)
        # Carry to be added in the next iter.
        carry = sum // 10

        # If this is the first node or head of linked list
        if temp is None:
            temp = head = node

        # For other nodes
        else:
            temp.next = ListNode
            temp = temp.next
    # We have to check if there is carry left
    # If carry exist, we have to create new node and add carry there
    if carry > 0:
        temp.next = ListNode(carry)
    return head
