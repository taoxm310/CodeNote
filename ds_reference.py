print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

# mylist 指向同一个对象的另一种名称
mylist = shoplist

# 删除第一项
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is',mylist)

# 注意到 shoplist 和 mylist 二者都
# 打印出了其中都没有 apple 的同样的列表，以此我们确认
# 它们指向的是同一个对象

print('Copy by making a full slice')
mylist = shoplist[:]

# 删除第一项
del mylist[0]
print('shoplist is', shoplist)
print('mylist is',mylist)
# 注意到现在两份列表已出现不同
