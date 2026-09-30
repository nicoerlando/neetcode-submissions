class Solution {
    public int[] getConcatenation(int[] nums) {
        int numsLen = nums.length;
        int[] concatenatedNums = new int[numsLen * 2];

        for (int i = 0; i < numsLen; i++){
            concatenatedNums[i] = nums[i];
            concatenatedNums[i + numsLen] = nums[i];
        }
        return concatenatedNums;
    }
}