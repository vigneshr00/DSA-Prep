# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if(target in nums):
        #     return nums.index(target)
        count = 0
        for i in range(len(nums)):
            if(nums[i] < target):
                count += 1
        return count

  
# 58. Length of Last Word
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s.rstrip()) - 1, -1, -1):
            if(s[i] == ' '):
                # count = 0
                break
            count += 1
        
        return count
           

    # 66. Plus One
    def plusOne(self, digits):
            """
            :type digits: List[int]
            :rtype: List[int]
            """
            result = ""
            for i in digits:
                result += str(i)

            result = int(result) + 1
            res = []
            for i in str(result):
                res.append(int(i))
            
            return res


    # 67. Add Binary
    def addBinary(self, a, b):
            """
            :type a: str
            :type b: str
            :rtype: str
            """
            i = len(a) - 1
            j = len(b) - 1
            carry = 0
            result = []
            while i>=0 or j>=0 or carry:
                total = carry
                if(i>=0):
                    total+=int(a[i])
                    i -= 1
                if(j>=0):
                    total += int(b[j])
                    j -= 1
                result.append(str(total % 2))
                carry = total // 2
                
            return "".join(reversed(result))
