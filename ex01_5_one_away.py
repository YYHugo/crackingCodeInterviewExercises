"""Chapter 01 Ex 05 One [change] away
    The program validate if one of these edits was performed:
    1- insert a char
    2- remove a char
    3- replace a char
    If any of these were done (and only once) return TRUE
"""
import unittest

def are_one_edit_away(str1, str2):
    """Given 2 strings, check if one of the three types of edits were done

    Args:
        str1 (string): one string
        str2 (string): another string
    """
    if len(str1) == len(str2):
        # possibly one replace
        return is_edit_replace(str1, str2)

    if len(str1) + 1 == len(str2):
        # possibly one insert in str1
        return is_edit_insert(str1, str2)
    if len(str1) == len(str2) + 1:
        # possibly one insert in str2
        return is_edit_insert(str2, str1)

    return False

def is_edit_replace(s1, s2):
    """Check if string was edited

    Args:
        s1 (string): one string
        s2 (string): another string same length

    Returns:
        Boolean: True if edited only once; False if no edition or more than one edition
    """

    if len(s1) != len(s2):
        return False

    edited = False
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            if edited:
                # it should enter only once, if another entrance, it means at least 2 replacements
                return False
            edited = True

    return edited

def is_edit_insert(s1, s2):
    """Iterate over each char to validate the change in an especific point

    Args:
        s1 (string): bigger string by 1 element
        s2 (string): smaller string by 1 element

    Returns:
        True if 's1' had 1 additional char than 's2'; the remaining chars are the same
        False if not
    """
    if len(s1) == len(s2):
        return False

    edited = False
    i = 0
    j = 0

    while (i < len(s1)) and \
            (j < len(s2)):

        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    # if everything worked so far up to this snippet, the last different char is the insert/removal
    return True

class Test(unittest.TestCase):
    test_cases = {
        # no changes
        ("pale", "pale"): False,
        ("", ""): False,
        # one insert
        ("pale", "ple"): True,
        ("ple", "pale"): True,
        ("pales", "pale"): True,
        ("ples", "pales"): True,
        ("pale", "pkle"): True,
        ("paleabc", "pleabc"): True,
        ("", "d"): True,
        ("d", "de"): True,
        # one replace
        ("pale", "bale"): True,
        ("a", "b"): True,
        ("pale", "ble"): False,
        # multiple replace
        ("pale", "bake"): False,
        # insert and replace
        ("pale", "pse"): False,
        ("pale", "pas"): False,
        ("pas", "pale"): False,
        ("pkle", "pable"): False,
        ("pal", "palks"): False,
        ("palks", "pal"): False,
        # permutation with insert shouldn't match
        ("ale", "elas"): False,
    }
    testable_functions = [are_one_edit_away]

    def test_one_away(self):
        for one_away_test in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = one_away_test(*args)
                assert actual == expected, f"Failed {one_away_test.__name__} for: {[*args]}, expected to be {expected} but we got {actual}"

if __name__ == "__main__":
    unittest.main()
