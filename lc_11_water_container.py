class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<2:
            return 0
        left = 0
        right = len(height)-1
        area = 0
        while left != right:
            area = max(area, (right - left) * min(height[right],height[left]))
            if height[left]> height[right]:
                right -=1
            elif height[left] < height[right]:
                left +=1
            else:
                right -=1
                left +=1
                if left > right:
                    break
        return area
