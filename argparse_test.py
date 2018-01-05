# -*- coding: cp936 -*-
import argparse
# 以下简单示例带有3个不同的选项：一个布尔选项（-a），一个简单的字符串选项（-b），以及一个整数选项（-c）。
parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print parser.parse_args(['-a', '-bval', '-c', '3'])

# “长”选项名字，即选项的名字多于一个字符，以相同的方式进行处理
parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--noarg', action="store_true", default=False)
parser.add_argument('--witharg', action="store", dest="witharg")
parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)

print parser.parse_args(['--noarg', '--witharg', 'val', '--witharg2=3'])

# 在这个例子中，“count”参数是一个整数，“units”参数存储为一个字符串。其中任意一个参数若没有在命令行中提供，或给定的值不能被转换为正确的类型，就会报告一个错误
parser = argparse.ArgumentParser(description='Example with non-optional arguments')

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print parser.parse_args()