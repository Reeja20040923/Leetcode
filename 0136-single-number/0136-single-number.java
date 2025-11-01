class Solution {
    public int singleNumber(int[] nums) {
        int indx=0;
        for(int i=0;i<nums.length;i++)
        {
            indx=indx^nums[i];
        }
        return indx;
    }
}