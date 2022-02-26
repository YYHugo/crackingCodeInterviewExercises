'''
    Check if a string is a permuted palindrome
'''
import unittest


# time complexity is O(N)
# space complexity is O(N)
def is_palindrome_permuted(string):
    '''
        by counting pairs of repeated chars
        there must be at most and only one occurance one letter that is odd
        the other letters must come in pairs (2, 4, 6, 8.... 2*k, k is positive integer)
    '''

    # counts how many odd letters there are
    countodd = 0
    # save occurances in array
    alphabet = [0] * (ord("z") - ord("a") + 1)
    # The given example "Tact Coa" showed that is case insensitive "C" == 'c'
    # Get string and lower() case
    s_lowered = string.lower()
