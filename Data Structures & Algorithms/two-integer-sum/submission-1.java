class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> indexToNumMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            indexToNumMap.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if (indexToNumMap.containsKey(diff) && indexToNumMap.get(diff) != i) {
                return new int[]{i, indexToNumMap.get(diff)};
            }
        }

        return new int[0];
        
    }
}
