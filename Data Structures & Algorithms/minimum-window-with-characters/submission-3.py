class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tMap = defaultdict()
        window = defaultdict()

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        have, need = 0, len(tMap)
        res = [-1, -1]
        resLen = float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if(c in tMap and window[c] == tMap[c]):
                have += 1
                
            while(have == need):
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] = window[s[l]] - 1
                if(s[l] in tMap and window[s[l]] < tMap[s[l]]):
                    have -= 1

                l += 1
            
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""





    




    

        

        