def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(50)
    1
    """
    if n % 50 == 0:
        return n // 50
    else:
        return n // 50 + 1

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0.05])
    (0.05, 0)
    >>> stock_price_summary([-0.03])
    (0, -0.03)
    >>> stock_price_summary([0.05, 0.03])
    (0.08, 0)
    >>> stock_price_summary([-0.03, -0.04, -0.06])
    (0, -0.13)
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    sumGains = 0
    sumLosses = 0

    for change in price_changes:
        if change > 0:
            sumGains = sumGains + change
        elif change < 0:
            sumLosses = sumLosses + change

    return (sumGains, sumLosses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> swap_k(nums, 1)
    >>> nums
    [2, 6, 3, 4, 1, 5]
    >>> swap_k(nums, 0)
    >>> nums
    [2, 6, 3, 4, 1, 5]
    """
    start = L[0:k]
    middle = L[k:-k]
    end = L[-k:]
    L[:] = end + middle + start

### alternative method, slower(tested) and less transparent
##    for i in range(k):
##        L[i], L[-k+i] = L[-k+i], L[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
