# -*- coding: cp936 -*-
# argparse内置6种动作可以在解析到一个参数时进行触发：
#
# store 保存参数值，可能会先将参数值转换成另一个数据类型。若没有显式指定动作，则默认为该动作。
#
# store_const 保存一个被定义为参数规格一部分的值，而不是一个来自参数解析而来的值。这通常用于实现非布尔值的命令行标记。
#
# store_ture/store_false 保存相应的布尔值。这两个动作被用于实现布尔开关。
#
# append 将值保存到一个列表中。若参数重复出现，则保存多个值。
#
# append_const 将一个定义在参数规格中的值保存到一个列表中。
#
# version 打印关于程序的版本信息，然后退出

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')

parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')

parser.add_argument('-a', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list')

parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()

print 'simple_value     =', results.simple_value
print 'constant_value   =', results.constant_value
print 'boolean_switch   =', results.boolean_switch
print 'collection       =', results.collection
print 'const_collection =', results.const_collection


# $ python argparse_action.py -h
#
# usage: argparse_action.py [-h] [-s SIMPLE_VALUE] [-c] [-t] [-f]
#                           [-a COLLECTION] [-A] [-B] [--version]
#
# optional arguments:
#   -h, --help       show this help message and exit
#   -s SIMPLE_VALUE  Store a simple value
#   -c               Store a constant value
#   -t               Set a switch to true
#   -f               Set a switch to false
#   -a COLLECTION    Add repeated values to a list
#   -A               Add different values to list
#   -B               Add different values to list
#   --version        show program's version number and exit
#
# $ python argparse_action.py -s value
#
# simple_value     = value
# constant_value   = None
# boolean_switch   = False
# collection       = []
# const_collection = []
#
# $ python argparse_action.py -c
#
# simple_value     = None
# constant_value   = value-to-store
# boolean_switch   = False
# collection       = []
# const_collection = []
#
# $ python argparse_action.py -t
#
# simple_value     = None
# constant_value   = None
# boolean_switch   = True
# collection       = []
# const_collection = []
#
# $ python argparse_action.py -f
#
# simple_value     = None
# constant_value   = None
# boolean_switch   = False
# collection       = []
# const_collection = []
#
# $ python argparse_action.py -a one -a two -a three
#
# simple_value     = None
# constant_value   = None
# boolean_switch   = False
# collection       = ['one', 'two', 'three']
# const_collection = []
#
# $ python argparse_action.py -B -A
#
# simple_value     = None
# constant_value   = None
# boolean_switch   = False
# collection       = []
# const_collection = ['value-2-to-append', 'value-1-to-append']
#
# $ python argparse_action.py --version
#
# argparse_action.py 1.0
