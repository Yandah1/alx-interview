#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x, nums):
    """
    Finds the winner after x rounds of the Prime Game.
    
    Args:
    x (int): Number of rounds.
    nums (list): List of n values for each round.
    
    Returns:
    str: Name of the player with the most wins or None if it's a tie.
    """
    if x < 1 or not nums:
        return None
    
    maria, ben = 0, 0

    # Create a list of prime numbers using the Sieve of Eratosthenes
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Count the number of primes for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben += primes_count % 2 == 0
        maria += primes_count % 2 == 1

    # Determine the overall winner
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'

