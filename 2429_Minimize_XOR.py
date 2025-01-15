"""
2429. Minimize XOR
Solved
Medium

Topics
Companies

Hint
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

 

Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
"""
class Solution:
    def countSetBits(self, number):
        count = 0
        while number != 0:
            count += (number & 1)
            number = number >> 1
        return count

    def addSetBits(self, number, bitsToAdd):
        bitPosition = 0
        while bitsToAdd > 0:
            while (number >> bitPosition) & 1 == 1:
                bitPosition += 1
            number = number | (1 << bitPosition)
            bitsToAdd -= 1
        return number

    def removeSetBits(self, number, bitsToRemove):
        while bitsToRemove > 0:
            number = number & (number - 1)
            bitsToRemove -= 1
        return number

    def minimizeXor(self, num1, num2):
        setBitsNum1 = self.countSetBits(num1)
        setBitsNum2 = self.countSetBits(num2)

        if setBitsNum1 == setBitsNum2:
            return num1
        if setBitsNum1 < setBitsNum2:
            return self.addSetBits(num1, setBitsNum2 - setBitsNum1)
        return self.removeSetBits(num1, setBitsNum1 - setBitsNum2)
