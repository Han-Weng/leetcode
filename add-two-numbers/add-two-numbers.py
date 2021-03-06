# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:    
            #check if the node has values
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            #check if the sum have carryovers
            #and adding the previous carryover
            #change the new carryover
            #the resultof the out will be added to the node
            carry, out = divmod(val1+val2 + carry, 10)    
            #
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next