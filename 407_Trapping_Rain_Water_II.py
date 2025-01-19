"""
407. Trapping Rain Water II
Solved
Hard

Topics
Companies
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
"""
class Solution:
    def trapRainWater(self, height: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(height), len(height[0])
        if m <= 2 or n <= 2:
            return 0
        boundary = []
        for i in range(m):
            boundary.append((height[i][0], i, 0))
            boundary.append((height[i][n - 1], i, n-1))
            height[i][0] = height[i][n-1] = -1
        for i in range(n):
            boundary.append((height[0][i], 0, i))
            boundary.append((height[m - 1][i], m - 1, i))
            height[0][i] = height[m-1][i] = -1
        heapify(boundary)
        ans, water_level = 0, 0
        while(boundary):
            h, i, j = heappop(boundary)
            water_level = max(water_level, h)
            for i_ in range(4):
                i0, j0 = i + dir[i_][0], j + dir[i_][1]
                if i0 < 0 or j0 < 0 or i0 >= m or j0 >= n or height[i0][j0] == -1:
                    continue
                currH = height[i0][j0]
                if currH < water_level:
                    ans += water_level - currH
                height[i0][j0] = -1
                heappush(boundary, (currH, i0, j0))
        return ans

