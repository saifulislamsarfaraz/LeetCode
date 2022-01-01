class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complementMap = dict()
        
        for i in range(len(nums)):
            num = nums[i]##2
            complement = target - num ##7
            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[complement] = i

           