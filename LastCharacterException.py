class LastCharacterException(Exception):
    """
    Exception raised for not having a digit as a last character

    Attributes:
        stringInput -- string provided for processing

    """
    def __init__(self, stringInput):
        self.stringInput = stringInput
        self.message = 'The last character must be a digit [0-9] not {}'.format(self.stringInput[-1])
        super().__init__(self.message)
        