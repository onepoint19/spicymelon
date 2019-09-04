class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff0 = nums[0] + nums[1] + nums[len(nums)-1] - target
        if len(nums) ==3:
            return target + diff0
        
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            
            diff = nums[i] + nums[j] + nums[k] - target
            if diff > 0:
                k -= 1
            elif diff <0:
                j +=1
            else:
                return target
            while j <k :
                diff1 = nums[i] + nums[j] + nums[k] - target
                if diff1 > 0:
                    k -= 1
                elif diff1 < 0:
                    j +=1
                else:
                    return target
                if abs(diff) > abs(diff1):
                    diff = diff1
                    
            if abs(diff0) > abs(diff):
                diff0 = diff
        return target + diff0    
                
