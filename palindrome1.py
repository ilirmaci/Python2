def is_palindrome_v1(word):
    """(str) -> bool

    Return True if and only if word is a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """

    return reverse(word) == word


def reverse(word):
    """(str) -> str

    Return a reversed version of word.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = '' #accummulator string

    # For each character in word, add that char to
    # the beginning of rev.

    for ch in word:
        rev = ch + rev

    return rev

if __name__ == '__main__':
    word = input('Enter a word: ')
    if is_palindrome_v1(word):
        print(word, 'is a palindrome.')
    else:
        print(word, 'is not a palindrome.')
    
   
