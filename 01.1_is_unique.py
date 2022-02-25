import unittest

def is_min_ASCII(string):
    # Assuming character set is ASCII (128 characters), if len(str) > 128, it means that there is repeated values
    # pow(2, 7) = 128 source: [Wikipedia] Originally based on the English alphabet, ASCII encodes 128 specified characters into seven-bit integers.
    if len(string) > 128:
        return False
    return True

# this method use an array to switch from false to true
# time complexity: O(N), where 'N = len(string)'
# Space complexity is O(N), where 'N = 128'
def is_unique_chars(string):
    if not is_min_ASCII(string):
        return False
    
    # interesting... multiplying single list
    # source: https://www.geeksforgeeks.org/python-boolean-list-initialization/
    char_set = [False] * 128;

    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

# AFAIR, there is bitwise operation in C, but I can't recall how it's used, but at least it avoids the use of array


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_chars,
    ]

    def test_is_unique_chars(self):
        # true check
        for unique_c in self.test_functions:
            for str, expected in self.test_cases:
                assert unique_c(str) == expected

if __name__ == "__main__":
    unittest.main()
