"""
82. Remove Duplicates from Sorted List II
Solved
Medium

Topics
Companies
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        temp = head
        prev = None
        dummy = ListNode(-1, head)
        prev = dummy
        val = prev.val
        a = []
        while(temp and temp.next):
            if temp.val != temp.next.val:
                prev.next = temp
                prev = temp
                temp = temp.next
            else:
                temp = temp.next
                a.append(temp.val)
        temp = dummy
        
        while(temp and temp.next):
            if temp.next.val in a:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next
                
                
                
