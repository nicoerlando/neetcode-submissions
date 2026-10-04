class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        dq = deque()
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while(dq and dq[-1][1] > heights[i]):
                heightPair = dq.pop()
                start = heightPair[0]
                maxArea = max(maxArea, (heightPair[1] * (i - start)))

            dq.append((start,heights[i]))
            
        while dq:
            heightPair = dq.pop()
            maxArea = max(maxArea, heightPair[1] * (len(heights) - heightPair[0]))

        return maxArea




        
        