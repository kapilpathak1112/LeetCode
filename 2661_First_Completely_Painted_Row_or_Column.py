"""
2661. First Completely Painted Row or Column
Solved
Medium

Topics
Companies

Hint
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
"""
class Solution:
    def firstCompleteIndex(self, arr, mat):
        n = len(arr)
        row, col = len(mat), len(mat[0])
        index = 0
        m1 = {}
        pos = [[0, 0] for _ in range(row * col + 1)]
        
        for i in range(row):
            for j in range(col):
                pos[mat[i][j]] = [i, j]
        
        while index < n:
            i, j = pos[arr[index]]
            m1['R' + str(i)] = m1.get('R' + str(i), 0) + 1
            m1['C' + str(j)] = m1.get('C' + str(j), 0) + 1
            if m1['R' + str(i)] == col or m1['C' + str(j)] == row:
                return index
            index += 1
        
        return -1
