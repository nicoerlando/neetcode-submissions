class Solution {
    public boolean isAnagram(String s, String t) {

        Map<String, Integer> charMap = new HashMap<>();

        for(char c : s.toCharArray()){
            if(charMap.containsKey(String.valueOf(c))){
                charMap.put(String.valueOf(c), charMap.get(String.valueOf(c)) + 1);
            } else {
                charMap.put(String.valueOf(c), 1);
            }
        }

        for(char c : t.toCharArray()){
            if(charMap.containsKey(String.valueOf(c))){
                charMap.put(String.valueOf(c), charMap.get(String.valueOf(c)) - 1);;
            } else {
                return false;
            }
        }

        for (int count : charMap.values()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }

}
