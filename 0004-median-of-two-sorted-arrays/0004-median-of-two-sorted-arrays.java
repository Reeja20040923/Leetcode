class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;

        int[] merge = new int[n+m];
        int r =0;
        for(int i=0;i<n;i++)
        {
            merge[r++] = nums1[i];
        }
        for(int i=0;i<m;i++)
        {
            merge[r++] = nums2[i];
        }
        Arrays.sort(merge);
        int merged = merge.length;
        if(merged%2==1)
        {
            return(double) merge[merged/2];
        }
        else
        {
            int middle1 = merge[merged/2-1];
            int middle2 = merge[merged/2];
            return((double) middle1 + (double) middle2)/2;
        }

        

        
    }
}