"""
23. Merge k Sorted Lists
Solved
Hard

Topics
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""
import heapq

class Solution(object):
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(nodes)
        root = node = ListNode()
        while(nodes):
            _, idx = heapq.heappop(nodes)
            curr = lists[idx]
            node.next = curr
            node = node.next
            if curr.next:
                lists[idx] = curr.next
                heapq.heappush(nodes, (curr.next.val, idx))
