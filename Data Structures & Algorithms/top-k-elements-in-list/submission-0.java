class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        List<Integer>[] freq = new List[nums.length + 1];
        Map<Integer, Integer> numToFreqMap = new HashMap<>();

        for(int n : nums){
            numToFreqMap.put(n, numToFreqMap.getOrDefault(n, 0) + 1);
        }

        for(int i = 0; i < nums.length + 1; i++){
            freq[i] = new ArrayList<>();
        }

        for(Map.Entry<Integer,Integer> entry: numToFreqMap.entrySet()){
            freq[entry.getValue()].add(entry.getKey());
        }
        System.out.println(Arrays.toString(freq));

        int[] res = new int[k];
        int index = 0;

        System.out.println(freq.length);
        for(int j = freq.length - 1; j > 0; j--){
            System.out.println(j);
            for(int num: freq[j]){
                System.out.println("freq.length");
                res[index++] = num;
                // index++;
                if(index == k){
                    return res;
                }
            }
        }
        return res;
    }
}
