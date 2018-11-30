# 引入模块，使用`sys.argv`访问变量`argv`
import sys
# 从模块中引入变量
from math import sqrt
print('The command line arguments are:')

for i in sys.argv:
    print(i)


print('\n\nThe PYTHONPATH is', sys.path, '\n')
print('Square root of 16 is', sqrt(16))
