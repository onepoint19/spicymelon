class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pm = []
        if len(nums) <= 1:
            pm.append(nums)
            return pm
        a = self.permute(nums[1:])
        for x in a:
            temp = [0] * len(x)
            temp[0:] = x
            temp.append(nums[0])
            pm.append(temp)
            for i in range(len(x)):
                temp = [0] * len(x)
                temp[0:] = x
                temp.append(x[i])
                temp[i] = nums[0]
                pm.append(temp)
            
        return pm
