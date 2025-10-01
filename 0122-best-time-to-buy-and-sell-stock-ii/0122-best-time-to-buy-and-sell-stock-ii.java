class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        
        for (int i=prices.length-2;i>=0;i--){
            if (prices[i+1]>prices[i]){
                profit += (prices[i+1]-prices[i]);
            }
        }
        return profit;
    }
}