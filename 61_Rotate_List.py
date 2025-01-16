"""
61. Rotate List
Solved
Medium

Topics
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getlength(self, node):
        temp = node
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count
    def rotateRight_(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        length = self.getlength(head)
        if k > length:
            k = k % length
        if k == 0 or (head.next is None) or k == length:
            return head        
        count = 0
        temp = head
        while(temp):
            count += 1
            if count == length - k:
                new_head = temp.next
                temp.next = None
                temp1 = new_head
                while(temp1.next):
                    temp1 = temp1.next
                temp1.next = head
                return new_head
            else:
                temp = temp.next

    def get_length(self, node):
        count = 0
        temp = node
        while(temp):
            temp = temp.next
            count += 1
        return count
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        length = self.get_length(head) 
        k = k % length
        if k == 0 or k == length or head.next is None:
            return head
        count = 0
        temp = head
        while(temp):
            count += 1
            if count == length - k:
                new_head = temp.next
                temp.next = None
                temp1 = new_head
                while(temp1.next):
                    temp1 = temp1.next
                temp1.next = head
                return new_head
            temp = temp.next
