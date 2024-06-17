#!/usr/bin/python3
'''Let check if a number is prime.'''


def isWinner(x, nums):
    '''Find the winner'''
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def playGame(n):
        primes = [num for num in range(2, n + 1) if isPrime(num)]
        maria_turn = True
        while primes:
            if maria_turn:
                pick = primes[0]
            else:
                pick = primes[-1]
            primes = [num for num in primes if num % pick != 0]
            maria_turn = not maria_turn
        return "Maria" if maria_turn else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = playGame(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
