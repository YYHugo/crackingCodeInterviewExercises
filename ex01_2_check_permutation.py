'''
    Chapter 01 ex 2 Cracking the code interview
    Check if string is a permutation of another string
'''

import unittest
def has_same_length(s_1, s_2):
    '''
        Shifting positions does not alter length. Different sizes implies no permutation
    '''
    if len(s_1) == len(s_2):
        return True

    return False

def check_permutation_by_sort(s_1, s_2):
    '''
        One way to solve it is to sort and check every i-th from string A w/ string B
        Time complexity: O(N log(N)), since sorted() is  n log n
        source:
        https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-the-sorted-function
        This is case-sensitive solution. You may use lower(), or use bit addition to convert A-Z to
        a-z
    '''
    if not has_same_length(s_1, s_2):
        return False

    s_1, s_2 = sorted(s_1), sorted(s_2)
    for i,elem in enumerate(s_1):
        if elem != s_2[i]:
            return False
    return True

def check_permutation_by_counting(s_1, s_2):
    '''
        Another way is to save every character (considering ASCII again w/ 128)

    '''
    if not has_same_length(s_1, s_2):
        return False

    letters_count = [0] * 128

    for character in s_1:
        letters_count[ord(character)] += 1

    for character in s_2:
        if letters_count[ord(character)] == 0:
            return False
        letters_count[ord(character)] -= 1

    return True


class Test(unittest.TestCase):
    '''
        Unit testing
    '''
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
        ("abcdee", "abcde", False),
    )

    testable_functions = [
        check_permutation_by_sort,
        check_permutation_by_counting,
    ]

    def test_check_permutation(self):
        '''
            Running unit testing
        '''
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
