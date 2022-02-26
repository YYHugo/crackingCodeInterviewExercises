'''
    URLify a string: substitute spaces for corresponding char %20 in HTTP requests
'''

import unittest

# Time complexity O(N)
# Space complexity O(N)
# since we're "expanding" current string, we may go from the end to the beginning

def urlify_string(string, length):
    '''
        Method to URLify
        Considering parameter string big enough to fit all substitutions: one space char is 3 chars
    '''
    # Python string are immutable
    # source: section "Deleting/Updating from a string" https://www.geeksforgeeks.org/python-strings
    # Changing into lists
    # source: https://docs.python.org/3/library/stdtypes.html#lists
    c_list  = list(string)
    new_index = len(c_list)

    # assuming that the string has enough length (and )last spaces)
    for i in reversed(range(length)):
        if c_list[i] == " ":
            # then replace spaces to %20
            c_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # move characters
            c_list[new_index - 1] = c_list[i]
            new_index-= 1
    # convert back to string
    return "".join(c_list[new_index:])


class Test(unittest.TestCase):
    '''
        Unit testing
    '''
    test_cases = {
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        ("   ", 1): "%20",
        ("abc-d efg  ", 9): "abc-d%20efg",
    }
    test_functions = [
        urlify_string,
    ]

    def test_urlify(self):
        '''
            Running unit testing
        '''
        for urlify_string_test in self.test_functions:
            for args, expected in self.test_cases.items():
                actual = urlify_string_test(*args)
                assert actual == expected, f"Failed {urlify_string.__name__} for: {[*args]}"


if __name__ == "__main__":
    unittest.main()
