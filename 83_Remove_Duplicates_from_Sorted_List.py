"""
83. Remove Duplicates from Sorted List
Solved
Easy

Topics
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        prev = ListNode(-1)
        prev.next = head
        while(temp):
            if prev.val == temp.val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head
