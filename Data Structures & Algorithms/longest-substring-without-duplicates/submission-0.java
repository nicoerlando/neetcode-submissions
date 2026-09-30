class Solution {
    public int lengthOfLongestSubstring(String s) {

        Map<Character, Integer> characterMap = new HashMap<>();
        int longest = 0;
        int l = 0;
        int r = 0;
        
        while (r < s.length()){
            if(characterMap.containsKey(s.charAt(r))){
                l = Math.max(characterMap.get(s.charAt(r)) + 1, l);
            }
            characterMap.put(s.charAt(r), r);
            longest = Math.max(longest, r - l + 1);
            r++;
        }
        return longest;
        
    }
}
