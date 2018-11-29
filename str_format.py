age = 20
name = 'time'
# 不省略index
print('{0} was {1} years old when he wrote this book'.format(name,age))

# 省略index
print('{} was {} years old when he wrote this book'.format(name,age))

# 用变量名
print('{name} was {age} years old when he wrote this book'.format(name=name,age=name))

# f-string
print(f'why is {name} playing with that python?')

# 对于浮点数 '0.333'，保留（.) 小数点后面三位
print('{0:.3f}'.format(1.0/3))

# fill with underscores(_) with the text centered
# (^) to 11 width '___hello___'
# 用_填充到长度为11，并保持文本处于中间
print('{0:_^11}'.format('hello'))

# keyword-based 基于关键字输出
print('{name} wrote {book}'.format(name ='Time', book='A Byte of Python'))

# 移除print 换行
print('a',end='')
print('b',end='')
