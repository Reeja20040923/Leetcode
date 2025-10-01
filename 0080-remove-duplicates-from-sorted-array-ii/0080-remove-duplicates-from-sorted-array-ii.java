class Solution {
    public int removeDuplicates(int[] nums) {
        

        if (nums.length<=2){
            return nums.length;
        }

        int start = 1;
        for (int i=2;i<nums.length;i++){
            if(nums[start-1] != nums[i]){
                nums[++start] = nums[i];
                
            }
        }
        return start + 1;
        
    }
}