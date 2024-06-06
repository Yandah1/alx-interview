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
    min_coins = [sys.maxsize for _ in range(total + 1)]
    min_coins[0] = 0  # Base case: 0 coins needed to make 0 total

    # Iterate through all amounts from 1 to total
    for current_amount in range(1, total + 1):
        # Check each coin
        for coin in coins:
            if coin <= current_amount:
                remaining_amount = current_amount - coin
                if min_coins[remaining_amount] != sys.maxsize:
                    min_coins[current_amount] = min(
                        min_coins[current_amount],
                        min_coins[remaining_amount] + 1)

    return -1 if min_coins[total] == sys.maxsize else min_coins[total]
