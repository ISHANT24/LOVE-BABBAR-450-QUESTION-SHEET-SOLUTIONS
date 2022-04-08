

class Solution:
    def count(self, S, m, n): 
        
        
        dp =[]                          #empty list for storing dp 
        for i in range(m+1):            #loop till m+1 
            a= [0]*(n+1)                
            dp.append(a)
            dp[i][0] = 1                # to et sum = 0 we only have 1 way by excluding the coins so 1
            
            
        
        
        
        for i in range(1, m+1):             # for filling rows
            for j in range(1, n+1):         #another loop within a row for filling columns of that row
            
                
                if S[i-1] > j:              # if the row value is greater than column value(sum value) then
                
                    dp[i][j] = dp[i-1][j]       #then we use the previous row or coin value to fill column with previous row value for that column
                    
                else:
                    
                    dp[i][j] = dp[i-1][j] + dp[i][j - S[i-1]]   #exclude that row and put values of previous row for that column and then include that row value / coin value by calculating row value - sum value then put the column values of that obtained calculated value /column value  
                                                                #means 3-3 = 0 so go to column 0 for row 3 and put the value of dp[3][0] in the included result and now sum of both included and excluded result in the column
                                                                
                                                                
                
                
        return dp[m][n]            
      
        


