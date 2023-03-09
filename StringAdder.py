from NoNegativeNumber2 import NoNegativeNumber
from NeedMoreNumbers import NeedMoreThanOneNumber
from LastCharacterException import LastCharacterException
import re


class StringAdder:
  
  """
  A class for the arithmetic addition of numbers found in a string.

  ...
  Methods
  -------
  Add(stringInput):
    Returns the sum of all numbers found in string
  
  """

  def __init__(self):

    """
    Constructs the necessary attributes of the StringAdder object   
    
    """
    self.stringInput = ''
    pass
   
  def Add(self, stringInput):
    """
    Extracts numbers from a string and then sums the numbers up

    Parameters
    ----------
    stringInput : str
                String having numbers to be processed
    
    Returns
    -------
    sum : int 
        sum of numbers found in the string

    """
    self.stringInput = stringInput.strip()
    
    if len(self.stringInput) == 0:
       return 0
    if len(re.findall(r'\d$', self.stringInput)) < 1: # validates that the final character of the string is a digit
      raise LastCharacterException(self.stringInput) 
    nums = re.split(r";|[,//|\n ([*% \] )]", self.stringInput)
    nums = [item for item in nums if item]

    if len(nums) < 2:
      raise NeedMoreThanOneNumber(nums) 
    sum = 0
    sumStr = "0"

    for id, x in enumerate(nums):
        
      if id != 0:
        sumStr += " +  {} ".format(str(x)) 
      else:
        sumStr = x
      x = int(x)
      if x < 0:
          raise NoNegativeNumber(x)
      elif(x >=1000):
         x = 0
      else:
            sum += x
    #print("{} = {}".format(sumStr, sum))
    return sum
  

