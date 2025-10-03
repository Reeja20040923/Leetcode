class Solution {
    public int maximumWealth(int[][] accounts) {
        int ans = 0;

        for (int[] i : accounts){
            int sum = 0;
            for (int money : i ){
                sum += money;
            }
            ans = Math.max(ans,sum);
        }
        return ans ;

    }
}