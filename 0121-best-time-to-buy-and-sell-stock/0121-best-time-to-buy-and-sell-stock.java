class Solution {
    public int maxProfit(int[] prices) {
        int min_price = prices[0];
        int profit = 0;

        for (int i=1;i<prices.length;i++){
            int cur_profit = prices[i]-min_price;

            if (cur_profit>profit){
                profit = cur_profit;
            }
            min_price = Math.min(prices[i],min_price);
        }
        return profit;
        




        
    }
}