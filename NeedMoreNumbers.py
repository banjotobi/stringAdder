class NeedMoreThanOneNumber(Exception):
    """
    Exception raised for attempting to add a single number

    Attributes:
        nums -- numbers gotten from string

    """
    def __init__(self, nums):
        self.nums = nums
        self.message = 'There should be at least two numbers in string'
        super().__init__(self.message)
