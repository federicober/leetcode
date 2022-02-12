class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = 0
        max_right = 0
        total_water = 0
        max_rights = [None] * len(height)
        for idx, h in enumerate(height[::-1]):
            if h > max_right:
                max_right = h
            max_rights[idx] = max_right
        max_rights = max_rights[::-1]
        for idx, h in enumerate(height):
            if h > max_left:
                max_left = h
            max_right = max_rights[idx]
            top_level = min(max_left, max_right)
            total_water += top_level - h
            # print(idx, "h", h, "left", max_left, "right", max_right, "top", top_level, total_water)
        return total_water
