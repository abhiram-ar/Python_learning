import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    # Any method that starts with test_ will be run automatically,
    # when we run test_name_function.py

    def test_first_last_name(self):
        """Do names like 'Abhiram Sajeev' works?"""

        formatted_name = get_formatted_name("abhiram", "sajeev")
        self.assertEqual(formatted_name, "Abhiram Sajeev")

    def test_first_last_middle_names(self):
        """Do names like 'Abhiram S Sajeev' work"""
        formatted_name = get_formatted_name("abhiram", "sajeev", "s")
        self.assertEqual(formatted_name, "Abhiram S Sajeev")


if __name__ == "__main__":
    unittest.main()
"""
We are going to run this file directly, but its important to note that many 
testing frameworks import your test files before running them. When a file 
is imported, the interpreter executes the file as its being imported.

looks at a special variable, __name__, which is set when the program is executed. 
If this file is being run as the main program, the value 
of __name__ is set to '__main__'. In this case, we call unittest.main(), which 
runs the test case. When a testing framework imports this file, the value of 
__name__ wont be '__main__' and this block will not be executed

"""
