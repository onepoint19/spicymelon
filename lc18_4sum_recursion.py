class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        r = self.NSum(nums, target, 4)
        return r
        
    def NSum(self, nums, target, N):
        nums.sort()
        ans = []
        if N == 2:
            i = 0
            j = len(nums)-1
            while i < j:
                s= nums[i] + nums[j]
                if s== target:
                    ans.append([nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1] and i < len(nums)-1:
                        i += 1
                    while nums[j] == nums[j+1] and j > 0:
                        j -= 1
                elif s > target:
                    j -= 1
                    while nums[j] == nums[j+1] and j > 0:
                        j -= 1
                elif s < target:
                    i += 1
                    while nums[i] == nums[i-1] and i < len(nums)-1:
                        i += 1
            return ans
        for i in range(len(nums)-N+1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ans1 = self.NSum(nums[i+1:],target - nums[i], N-1)
            for x in ans1:
                x.append(nums[i])
                ans.append(x)
        return ans
