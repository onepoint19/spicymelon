class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            if i>0 and nums[i]== nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = len(nums)-1
                while k < l:
                    s = nums[i]+nums[j]+nums[k]+nums[l]
                    if s == target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        while nums[k] == nums[k-1] and k < len(nums)-1:
                            k += 1
                        l -=1
                        while nums[l] == nums[l+1] and l > j+1:
                            l -= 1
                    elif s > target:
                        l -= 1
                        while nums[l] == nums[l+1] and l > j+1:
                            l -= 1

                    elif s < target:
                        k += 1
                        while nums[k] == nums[k-1] and k < len(nums)-1:
                            k += 1
        return ans
