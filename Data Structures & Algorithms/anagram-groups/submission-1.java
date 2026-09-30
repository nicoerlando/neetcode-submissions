class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> resultMap = new HashMap<>();
        for(String str: strs){
            int[] count = new int[26];
            for (char c: str.toCharArray()){
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            resultMap.putIfAbsent(key, new ArrayList<>());
            resultMap.get(key).add(str);
        }
        return new ArrayList<>(resultMap.values());
    }
}
