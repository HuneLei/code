#-*- coding: utf-8 -*-
import argparse

# 另一种自己处理配置文件的方法是使用fromfile_prefix_chars指定
# 一个包含一组要待处理参数的输入文件来告诉argparse怎样识别参数

parser = argparse.ArgumentParser(description='Short sample app',
                                 fromfile_prefix_chars='@'
                                 )

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print parser.parse_args(['@argparse_fromfile_prefix_chars.txt'])
