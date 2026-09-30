class Solution {
    public boolean hasDuplicate(int[] nums) {

        Map<Integer, Integer> numberMap = new HashMap<>();

        for (Integer num: nums){
            if(numberMap.containsKey(num)){
                return true;
            } else {
                numberMap.put(num, 1);
            }
        }
        return false;
        
    }

}