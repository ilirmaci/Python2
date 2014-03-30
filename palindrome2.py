import palindrome1

def is_palindrome_v2(word):
    """(str) -> bool

    Return True if and only if word is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """

    # The number of characters in word
    n = len(word)

    # Compare the first half of word to the reverse of its second half
    # Omit middle character if n is odd
    return word[:n//2] == reverse(word[n - n//2:])

##def reverse(word):
##    """(str) -> str
##
##    Return a reversed version of word.
##
##    >>> reverse('hello')
##    'olleh'
##    >>> reverse('a')
##    'a'
##    """
##
##    rev = '' #accummulator string
##
##    # For each character in word, add that char to
##    # the beginning of rev.
##
##    for ch in word:
##        rev = ch + rev
##
##    return rev
