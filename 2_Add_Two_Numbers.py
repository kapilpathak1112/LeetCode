"""
2. Add Two Numbers
Solved
Medium

Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        start = temp
        carry = 0
        while(l1 and l2):
            total = l1.val + l2.val + carry
            reminder = total % 10
            carry = total // 10
            temp.next = ListNode(reminder)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        if l1 is None:
            while(l2):
                total = l2.val + carry 
                reminder = total % 10
                carry = total // 10
                temp.next = ListNode(reminder)
                temp = temp.next
                l2 = l2.next

        if l2 is None:
            while(l1):
                total = l1.val + carry 
                reminder = total % 10
                carry = total // 10
                temp.next = ListNode(reminder)
                temp = temp.next
                l1 = l1.next
        if carry > 0:
            temp.next = ListNode(carry)

        return start.next
