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
# 4. 将当前日期作为主备份目录下的子目录名
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')

# zip 文件名称格式
target = today + os.sep + now + '.zip'
if not os.path.exists(today):
    os.mkdir(today) # 创建目录
    print('Successfully created directory', today)

# 5. 使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is: ')
print(zip_command)
print('Running: ')
if os.system(zip_command) == 0: # 如果成功返回0 失误返回错误代码
    print('Successful backup to', target)
else:
    print('Backup FAILED')
