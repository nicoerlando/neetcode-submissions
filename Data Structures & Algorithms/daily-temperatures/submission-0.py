class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        dq = deque()
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while(dq and temperatures[dq[-1]] < temperatures[i]):
                day = dq.pop()
                result[day] = i - day
                
            dq.append(i)

        return result



        