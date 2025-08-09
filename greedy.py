#!/usr/bin/python3
""" greedy Algorithm """


def greedy(price, available_coins):
    """
    Return coins to make price using greedy method.
    Returns [] if not possible.
    """
    coins = []
    next_coin = 0
    remaining_price = price
    sorted_coins = sorted(
        set(available_coins), reverse=True
    )
    if 0 in sorted_coins:
        sorted_coins.remove(0)

    if price < sorted_coins[-1]:
        return []
    while remaining_price:
        if next_coin >= len(sorted_coins):
            return []
        maxv = sorted_coins[next_coin]
        if maxv > remaining_price:
            next_coin += 1
        else:
            remaining_price -= maxv
            coins.append(maxv)
    return coins


print(greedy(30, [25, 10, 5, 1]))
print(greedy(3, [5, 10, 25]))
print(greedy(0, [1, 2, 5]))
print(greedy(7, [2, 4]))
print(greedy(11, [1, 5, 7]))
