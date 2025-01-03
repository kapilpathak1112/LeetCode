"""
19. Remove Nth Node From End of List
Solved
Medium

Topics
Companies

Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head):
        count = 0
        temp = head
        while(temp):
            temp = temp.next
            count += 1
        return count
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = self.getLength(head)
        if N == 1 and n == 1:
            return None
        if N == n:
            return head.next
        NnthNode = N-n -1
        count = 0
        temp = head
        while(count != NnthNode):
            temp = temp.next
            count += 1
        if temp.next:
            temp.next = temp.next.next
        return head
