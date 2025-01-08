"""
21. Merge Two Sorted Lists
Solved
Easy

Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        start = ListNode(0)
        temp = start
        while(temp1 and temp2):
            if temp1.val >= temp2.val:
                temp.next = temp2
                temp = temp.next
                temp2 = temp2.next
            else:
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
        while(temp1):
            temp.next = temp1
            temp = temp.next
            temp1 = temp1.next
        while(temp2):
            temp.next = temp2
            temp = temp.next
            temp2 = temp2.next
        return start.next
