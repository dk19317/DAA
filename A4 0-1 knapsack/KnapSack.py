def knapsack_dp(weights, values, W):
    n = len(values)
    
    # Initialize DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # The maximum value will be in dp[n][W]
    return dp[n][W]

# Example usage
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7
max_value = knapsack_dp(weights, values, W)
print(f"Maximum value in Knapsack = {max_value}")

