"""String compression
"""
import unittest

def compress_string(string):
    """method that compress string, if a shorter string is done w/ representing the repetition of sabe char
    case insensitive (only lower case)
    Args:
        string (string): string to be compressed
    """
    compressed = []
    count = 0
    s  = string.lower()

    for i,c in enumerate(s):
        if c != s[i - 1]:
            compressed.append(s[i - 1] + str(count))
            count = 0
        count += 1

    if count:
        compressed.append(s[-1] + str(count))
    
    print("".join(compressed))
    
    return min(s, "".join(compressed), key=len)

class Test(unittest.TestCase):
    """
        Unit testing
    """
    test_cases = {
        ("aabcccccaaa"): "a2b1c5a3",
        ("abcdef"): "abcdef",
        ("aabb"): "aabb",
        ("aaa"): "a3",
        ("a"): "a",
        (""): "",
        ("aabccCccaAa"): "a2b1c5a3"
    }
    testable_functions = [
        compress_string,
    ]

    def test_string_compression(self):
        """
            Running unit testing
        """
        for f in self.testable_functions:
            for string, expected in self.test_cases.items():
                actual = f(string)
                assert actual == expected, f"Failed {f.__name__} for: {string}, expecting {expected} but we've got {actual}"


if __name__ == "__main__":
    unittest.main()
