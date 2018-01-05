# -*- coding: utf-8 -*-
import ConfigParser
import sys

config = ConfigParser.ConfigParser()
config.add_section("book")
config.set("book", "title", "这是标题")
config.set("book", "author", "蓝胖子")
config.add_section("size")
config.set("size", "size", "1024")
config.write(sys.stdout)
config.write(open('writetest.ini', 'a'))

# sys.stdout 标准输出
# print config.options("book")
# print config.options("size")
# print config.get("book", config.options("book")[0])

# 1、config = ConfigParser.ConfigParser()
# 创建ConfigParser实例
#
# 2、config.sections()
# 返回配置文件中节序列
#
# 3、config.options(section)
# 返回某个项目中的所有键的序列
#
# 4、config.get(section, option)
# 返回section节中，option的键值
#
# 5、config.add_section(str)
# 添加一个配置文件节点(str)
#
# 6、config.set(section, option, val)
# 设置section节点中，键名为option的值(val)
#
# 7、config.read(filename)
# 读取配置文件
#
# 8、config.write(obj_file)
# 写入配置文件
