#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):
    if n == 1:
        return 0
    
    # Initialize a list to store minimum operations needed for each state
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    # Iterate through each state and update the minimum operations needed
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]