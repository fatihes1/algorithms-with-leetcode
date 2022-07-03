class Solution:
    #For example we have linked list like 3 -> 4-> 5-> 6-> 7->8 . I want to delete 7
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head # I created this variable for find the length of the list
        lengthOfLinkedList=0

        while temp!=None: # find the length of the linked list
            lengthOfLinkedList+=1
            temp=temp.next

        if lengthOfLinkedList==1 and n==1:  # Deleting only node in list
            head=head.next
            return head

        if lengthOfLinkedList>1:  # while there are more than one node in  linked list
            if n!=lengthOfLinkedList:   # if n== length of list that means we delete node from at the beginning of list
                deleted=head # create variable "deleted" which will be deleted from list later on
                lengthOfLinkedList=lengthOfLinkedList-n

                while lengthOfLinkedList>0:
                    prev=deleted  # You can think that prev is kinda pointer which points previous node from deleted node so if I want to delete 7 then prev node will point to 6
                    deleted=deleted.next   # equal to 7

                    lengthOfLinkedList=lengthOfLinkedList-1

                prev.next=deleted.next  ##deleting operation happening here  I set prev.next to deleted next  Which means 6 -> 8   as you see deleted.next equals to 8
                deleted.next=None  #   7->None
                return head # We deleted the node and return the new Linked list
            else:  # delete node from beginning of list
                return head.next
