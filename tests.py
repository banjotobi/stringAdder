import unittest
from StringAdder import StringAdder
from NoNegativeNumber2 import NoNegativeNumber
from LastCharacterException import LastCharacterException

class TestSum(unittest.TestCase):
    a = StringAdder()
    def testReq1a(self):
        """
        The method will return the sum of comma-separated integer numbers parsed from the numbers parameter (for an empty string it will return 0).
        """
        self.assertEqual(self.a.Add(""), 0, "Should be 0")
    
    def testReq1ai(self):
        """
        The method will return the sum of comma-separated integer numbers parsed from the numbers parameter
        """
        self.assertEqual(self.a.Add("1,2"), 3, "Should be 3")
    
    def testReq2a(self):
        """
        In addition to commas, allow the Add method to handle new lines between numbers.
        The following input is ok:  
        “1\n2,3”

        """
        self.assertEqual(self.a.Add("1\n2,3"), 6, "Should be 6")
        
    def testReq2b(self):
        """
        In addition to commas, allow the Add method to handle new lines between numbers
        The following input is NOT ok: 
        “1,\n”
        """
        with self.assertRaises(LastCharacterException):
            self.a.Add("1,\n")
    
    def testReq3a(self):
        """
        As well as comma-separated and new lines, allow the Add method to support different delimiters
        To set the delimiter, the beginning of the input string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]
        
        """
        self.assertEqual(self.a.Add("//;\n1;2"), 3, "Should be 3")

    def testReq4(self):
        """
        The Add method when called with a negative number will throw an exception “negatives not allowed”. The exception string should include a comma-separated list of each negative number passed to the Add method
        """
        with self.assertRaises(NoNegativeNumber):
            self.a.Add("1,\n-2")
    
    def testReq5(self):
        """
        The Add method should ignore any numbers bigger than 1000, so adding 2 + 1001 = 2
        """
        self.assertEqual(self.a.Add("//;\n2;1000"), 2, "Should be 2")

    def testReq6(self):
        """
        Allow the Add method to support Delimiters of any length with the following format: 
        “//[delimiter]\n” 
        """
        self.assertEqual(self.a.Add("//[***]\n1***2***3"), 6, "Should be 6")

    def testReq7(self):
        """
        In addition to point 6, allow the Add method to support multiple delimiters like this: 
        “//[delim1][delim2]\n”
        """
        self.assertEqual(self.a.Add("//[*][%]\n1*2%3"), 6, "Should be 6")
    
    def testReq8(self):
        """
        In addition to point 7, allow the Add method to support multiple delimiters of any length like this:
        “//[delim1][delim2]\n”
        """
        self.assertEqual(self.a.Add("//[**][%%%]\n1**2%%%3"), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()