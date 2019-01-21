class Solution():
# Ex1
#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
#design an algorithm to find the maximum profit.
#Note that you cannot sell a stock before you buy one.

    def max_profit(self,prices):
        if not prices or len(prices)==1:
            return 0
        max_profit=0
        buy_price=prices[0]
        for i in range(0,len(prices)):
            if prices[i]>buy_price:
                max_profit=max(max_profit,prices[i]-buy_price)
                prev=prices[i]
            else:
                buy_price=prices[i]
            prev=prices[i]
        return max_profit

#Ex2
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
# money you can rob tonight without alerting the police.

    def rob_house(self,money_in_houses):
        if not money_in_houses:
            return 0
        if len(money_in_houses)<=2:
            return max(money_in_houses)
        result=[0]*money_in_houses
        result[0]=money_in_houses[0]
        result[1]=max(result[0],result[1])
        for i in range(2,len(money_in_houses)):
            result[i]=max(result[i-1],result[i-2]+money_in_houses[i])
        return result[-1]



if __name__=='__main__':
    o_solution=Solution()
    i_max_profit=o_solution.max_profit(prices=[3,6,7,3,1,8])
    print('The end')