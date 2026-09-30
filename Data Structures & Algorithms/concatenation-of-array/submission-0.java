class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] concatenatedNums = new int[nums.length * 2];
        int numsLen = nums.length;

        for (int i = 0; i < numsLen; i++){
            concatenatedNums[i] = nums[i];
            concatenatedNums[i + numsLen] = nums[i];
        }
        return concatenatedNums;
    }
}