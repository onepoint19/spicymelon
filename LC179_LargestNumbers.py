class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
            return ''
        nums_sort = sorted(nums, cmp = self.gt)
        if nums_sort[0] == 0:
            return '0'

        return (''.join(map(str,nums_sort)))
        
    def gt(self, x , y):
        a = int(str(x) + str(y))
        b = int(str(y) + str(x))
        if a > b:
            return -1
        if a == b:
            return 0
        return 1
