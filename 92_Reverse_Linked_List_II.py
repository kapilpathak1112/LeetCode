"""
92. Reverse Linked List II
Solved
Medium

Topics
Companies
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head  
        root = ListNode()
        root.next = head

        start = root
        for _ in range(left - 1):
            start = start.next

        cur = start.next
        pre = None
        for _ in range(right - left + 1):
            cur.next, pre, cur = pre, cur, cur.next
        start.next.next = cur # According to the example, 2->5
        start.next = pre # According to the example, 1->4
        return root.next
            
                
