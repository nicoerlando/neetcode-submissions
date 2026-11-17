class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = list(count.values())
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                newCount = heapq.heappop_max(maxHeap) - 1
                if newCount:
                    q.append([newCount, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])

        
        return time



        