shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'

# indexing
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Character 0 is', name[0])

# slicing on list
print('Item 1 to 3', shoplist[1:3])
print('Item 2 to end ', shoplist[2:])
print('Item 1 to -1 ', shoplist[1:-1])
print('Item start to end ', shoplist[:])

# slicing on string
print('characters 1 to 3', name[1:3])
print('characters 2 to end ', name[2:])
print('characters 1 to -1 ', name[1:-1])
print('characters start to end ', name[:])
