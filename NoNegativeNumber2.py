class NoNegativeNumber(Exception):
    """
    Exception raised for errors in the numbers being added

    Attributes:
        num -- negative number found in string

    """
    def __init__(self, num):
        self.num = num
        self.message = 'negatives not allowed'
        super().__init__(self.message)
