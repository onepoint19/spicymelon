# leetcode 15
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        nums.sort()
        # print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                # print('i, j, k: ', i,j,k)
                # print('nums: ', nums[i], nums[j], nums[k])
                sum3 = nums[i] + nums[j] + nums[k] 
                if sum3 > 0:
                    k -= 1
                    while k>i and nums[k] == nums[k+1]:
                        k -= 1
                if sum3 < 0:
                    j += 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
                if sum3 == 0:
                    sol.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -=1
                    while k > i and nums[k] == nums[k+1]:
                        k -= 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
        return sol
