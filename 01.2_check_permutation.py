import unittest

def has_same_length(s1, s2):
    if len(s1) == len(s2):
        return True

    return False

# One way to solve it is to sort and check every i-th from string A w/ string B
# Time complexity: O(N log(N)), since sorted() is  n log n
# source https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-the-sorted-function
# This is case-sensitive solution. You may use lower(), or use bit addition to convert A-Z to a-z
def check_permutation_by_sort(s1, s2):
    if not has_same_length(s1, s2):
        return False

    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

# Another way is to save every character (considering ASCII again w/ 128)
def check_permutation_by_counting(s1, s2):
    if not has_same_length(s1, s2):
        return False

    letters_count = [0] * 128

    for c in s1:
        letters_count[ord(c)] += 1
    
    for c in s2:
        if letters_count[ord(c)] == 0:
            return False
        letters_count[ord(c)] -= 1

    return True


class Test(unittest.TestCase):
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

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
