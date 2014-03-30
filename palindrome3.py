def is_palindrome_v3(word):
    """(str) -> bool

    Return True if and only if word is a palindrome.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """

    # i starts at first index of word, j starts at last
    i = 0
    j = len(word) - 1

    while i < j and word[i] == word[j]:
        i = i + 1
        j = j - 1

    return j <= i
