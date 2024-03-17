def is_palindrome(str):
    starting = 0 #  Start index of the string.
    ending = len(str) - 1 #  set the second pointer to point at the last character

    while starting < ending:
        if str[starting] != str[ending]: #  If the characters don't match, it isn't a palindrome.
            return False

        starting += 1
        ending -= 1

    return True
