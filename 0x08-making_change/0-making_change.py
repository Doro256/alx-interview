#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """
    Function to determine the fewest number of coins needed to
    meet a given amount total
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for c in coins:
        for i in range(c, total + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[total] if dp[total] != float('inf') else -1
