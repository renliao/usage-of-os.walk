'''
该代码用来解释python中的os.walk()函数的用法
代码参考来源：https://zhuanlan.zhihu.com/p/149824829
所需的测试文件夹为：dir_path
'''
import os 
dir_path="C:\\Users\\admin\\Desktop\\VOC2YOLO\\Test_oswalk"
#默认自外层向里层递归地扫描dir_path文件夹
for curDir, subdirs, files in os.walk(dir_path):
    print("<<==============================>>")
    print("现在的目录：" + curDir)
    print("该目录下包含的子目录：" + str(subdirs))
    print("该目录下包含的文件：" + str(files))
# 如果想要自里层向外层扫描子目录和文件，可以添加上topdown=False参数
for curDir, subdirs, files in os.walk(dir_path,topdown=False):
    print("<<==============================>>")
    print("现在的目录：" + curDir)
    print("该目录下包含的子目录：" + str(subdirs))
    print("该目录下包含的文件：" + str(files))
#输出当前文件夹下的所有文件
for curDir, dirs, files in os.walk(dir_path):
    for file in files:
        print(os.path.join(curDir, file))
#输出当前文件夹下指定后缀名地（比如.txt）文件
for curDir, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(curDir, file))
#输出当前文件夹下所有的子目录（子文件夹），包含子目录里的子目录
for curDir, dirs, files in os.walk(dir_path):
    for dir in dirs:
        print(dir)
