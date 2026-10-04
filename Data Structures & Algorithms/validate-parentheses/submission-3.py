class Solution:
    def isValid(self, s: str) -> bool:

        dq = deque()
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for i in range(len(s)):
            if s[i] in closeToOpen:
                if(dq and dq[-1] == closeToOpen[s[i]]):
                    dq.pop()
                else: 
                    return False
            else:
                dq.append(s[i])

        return not dq

            
        