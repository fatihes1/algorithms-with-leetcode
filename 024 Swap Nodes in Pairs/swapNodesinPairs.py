# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp!=None and temp.next!=None:
            currNodeValue= temp.val
            nextNodeValue=temp.next.val

            temp.val=nextNodeValue
            temp.next.val=currNodeValue

            temp=temp.next.next


        return head
