class Solution {
    public void sortColors(int[] nums) {
        int l = 0;
        int i = 0;
        int r = nums.length - 1;

        while(i <= r){
            if(nums[i] == 0){
                swap(nums, i, l);
                l++;
            }

            if(nums[i] == 2){
                swap(nums, i, r);
                r--;
                i--;
            }
            i++;
        }   
        return;

    }

    private void swap(int[] nums, int i, int j){
        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;
    }
      
}