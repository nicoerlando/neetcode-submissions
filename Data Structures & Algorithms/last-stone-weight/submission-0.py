class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1, stone2 = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if stone2 == stone1:
                continue
            elif stone2 > stone1:
                heapq.heappush_max(stones, stone2 - stone1)
            else:
                heapq.heappush_max(stones, stone1 - stone2)

        if len(stones) == 0:
            return 0
        else: 
            return stones[0]