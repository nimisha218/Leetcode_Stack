class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # List of [index, height] lists
        max_area = 0

        for i, h in enumerate(heights):

            index, height = i, heights[i]

            start = index
            
            while stack and height < stack[-1][1]:
                # Pop the top most element from the stack
                prev_index, prev_height = stack.pop()
                # As we pop it, also compute the maximum area it could've computed
                max_area = max(max_area, (index - prev_index) * prev_height)
                # prev_index = 0
                # prev_height = 2
                # height < prev_height
                start = prev_index
            
            stack.append([start, height])
            max_area = max(max_area, height)
    
        for ih in stack:

            curr_area = (len(heights) - ih[0]) * ih[1]
            max_area = max(max_area, curr_area)

        return max_area

