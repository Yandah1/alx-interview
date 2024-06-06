#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount total.
"""
import sys


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    # Initialize a table to store the minimum coins needed for each amount
    min_coins = [sys.maxsize] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins needed to make 0 total

    # Iterate through all coins and update the min_coins table
    for coin in coins:
        for amount in range(coin, total + 1):
            if min_coins[amount - coin] != sys.maxsize:
                min_coins[amount] = min(min_coins[amount],
                                        min_coins[amount - coin] + 1)

    return -1 if min_coins[total] == sys.maxsize else min_coins[total]
