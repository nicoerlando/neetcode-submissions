class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        dq = deque()

        for p,s in pair:
            time = (target - p)/s
            if(dq and dq[-1] >= time):
                continue
            dq.append(time)
        
        return len(dq)
            
        
        