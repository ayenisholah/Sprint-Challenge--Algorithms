'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    n = len(word)
    # Base case
    if (n == 0 or n < 2):
        return 0
        # Recursive Case
        # Check if the first substring matches
    if (word[0:2] == 'th'):
        return 1 + count_th(word[1:])
        # Otherwise return the count
        # from the remaining index
    return count_th(word[1:])


count_th('th')