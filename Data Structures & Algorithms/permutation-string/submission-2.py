class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if(len(s2) < len(s1)):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] = s1Count[ord(s1[i]) - ord('a')] + 1
            s2Count[ord(s2[i]) - ord('a')] = s2Count[ord(s2[i]) - ord('a')] + 1

        i = 0
        j = len(s1) - 1

        if s1Count == s2Count:
                return True

        while j < len(s2) - 1:
            s2Count[ord(s2[i]) - ord('a')] = s2Count[ord(s2[i]) - ord('a')] - 1
            i += 1
            j += 1
            s2Count[ord(s2[j]) - ord('a')] = s2Count[ord(s2[j]) - ord('a')] + 1

            if s1Count == s2Count:
                return True
                
        return False

                

