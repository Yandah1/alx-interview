#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i])
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n):
    '''To find round winner'''
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num
        if prime == -1:
            return players[(i + 1) % 2]
        else:
            for idx in sorted(selectedIdxs, reverse=True):
                del list[idx]
    return None


def isPrime(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return False
        return True
