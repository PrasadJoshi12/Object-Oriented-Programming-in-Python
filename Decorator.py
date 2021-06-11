# Decorator Example
class Error_check:
  def __init__(self, function):
    self.function = function 
  def __call__(self, *args):
    if any([isinstance(i, str) for i in args]):
      raise Exception("Please Enter the Numeric Value")
    else:
      return self.function(args)
      
@Error_check
def add_num(args):
  return sum(args)

print(add_num(1,2,3,4))
  
#Output:
10
