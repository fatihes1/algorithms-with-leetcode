# Function params => l1: Optional[ListNode], l2: Optional[ListNode]
# Data type that the function returns => Optional[ListNode]

def addTwoNumbers(l1, l2):
    node = ListNode()
    current = node

    carry = 0
    while l1 or l2 or carry:
        value1 = l1.val if l1 else 0
        value2 = l2.val if l2 else 0

        # new digit
        value = value1 + value2 + carry
        # if one digit + one digit number = two digit number ?
        carry = value  // 10
        value = value % 10

        current.next = ListNode(value)

        # Update current pointers
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return node.next
