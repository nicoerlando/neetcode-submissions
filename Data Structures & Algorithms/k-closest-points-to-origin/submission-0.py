class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        for point in points:
            distance = self.calculateDistance(point[0], point[1])
            minHeap.append([distance, point[0], point[1]])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        
        return res

    def calculateDistance(self,x, y):
        return (x**2 + y**2)

        