# -*- coding: cp936 -*-
# 目前为止所见的例子中，提供给解析器的参数列表来自于显式传递的一个列表，或隐式地从sys.argv获取的。
# 显式传递列表在你使用argparse来处理类命令行但并不是来自命令行（比如来自一个配置文件）的指令之时比较有用
import argparse
from ConfigParser import ConfigParser
import shlex

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

config = ConfigParser()
config.read('argparse_witH_shlex.ini')
config_value = config.get('cli', 'options')
print 'Config: ', config_value
argument_list = shlex.split(config_value)
print 'Arg List:', argument_list
print 'Results:', parser.parse_args(argument_list)
