# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left <= right:
            pivot = left + (right - left) // 2
            if isBadVersion(pivot) == True:
               right = pivot - 1
            else:
                left = pivot + 1
        return left
                
                