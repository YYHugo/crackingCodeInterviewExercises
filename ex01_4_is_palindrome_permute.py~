'''
    Check if a string is a permuted palindrome
'''
from string import printable
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
    # save occurences in array
    alphabet = [0] * (ord("z") - ord("a") + 1)
    # The given example "Tact Coa" showed that is case insensitive "C" == 'c'
    # But are we considering the use of other chars, like ! , . > ?
    # lower() case the string
    s_lowered = string.lower()

    for c in s_lowered:
        i = c_number(c)
        if i != -1:
            alphabet[i] += 1
            if alphabet[i] % 2:
                countodd += 1
            else:
                countodd -= 1
        else:
            print("countodd: " + str(countodd))
            return False

    return countodd <=1

def c_number(c):
    '''
        Return the position of character 'c' in alphabet
    '''
    first = ord("a")
    val = ord(c)
    last = ord("z")
    
    # check only letters
    if first <= val <= last:
        return (val - first)
    # not a letter
    return -1
    
class Test(unittest.TestCase):
    '''
        Unit testing
    '''
    test_cases = {
        ("aba"): True,
        ("aab"): True,
        ("abba"): True,
        ("aabb"): True,
        ("a-bba"): True,
        ("Tact Coa"): True,
        ("jhsabckuj ahjsbckj"): True,
        ("Able was I ere I saw Elba"): True,
        ("So patient a nurse to nurse a patient so"): False,
        ("Random Words"): False,
        ("Not a Palindrome"): False,
        ("no x in nixon"): True,
        ("azAZ"): True,
        (""): True,
        ("1221"): True,
        ("aba>"): True
    }
    testable_functions = [
        is_palindrome_permuted,
    ]
    def test_is_palindrome(self):
        '''
            Running unit testing
        '''
        for f in self.testable_functions:
            for [args, expected] in self.test_cases.items():
                actual = f(args)
                assert actual == expected, f"Failed {f.__name__} for input: {[args]}, expecting {expected} but we've got {actual}"

if __name__ == "__main__":
    unittest.main()
