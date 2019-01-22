# encoding = UTF-8

class ShortInputExceptions(Exception):
    """用户定义的异常类"""
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputExceptions(len(text), 3)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputExceptions as ex:
    print(('ShortInputException: The input was ' + '{0} long, expected at least {1}').format(ex.length,ex.atleast))
else:
    print('No exception was raised')
