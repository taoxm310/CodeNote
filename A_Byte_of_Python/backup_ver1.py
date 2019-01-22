import os
import time

# 1. 需要备份的文件和目录都将被指定在一个列表里。
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = ['/Users/bfc04/notes']
# 对于包含空格的名称，需要在字符串中使用双引号

# 2. 备份文件必须存储在一个主备份目录中
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/bfc04/backup'

# 3. 备份文件将打包压缩成zip文件
# 4. zip压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

# 5. 使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is: ')
print(zip_command)
print('Running: ')
if os.system(zip_command) == 0: # 如果成功返回0 失误返回错误代码
    print('Successful backup to', target)
else:
    print('Backup FAILED')
