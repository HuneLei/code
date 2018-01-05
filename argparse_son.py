# -*- coding: utf-8 -*-
# 我们常常需要实现一套命令行程序，这些程序都带一组参数，只是在某些方面有特殊化。例如，
# 如果所有程序都需要在用户进行任何实际的操作之前对用户进行认证，那么它们就都需要支持--user和--password选项。
# 你可以共享的选项来定义一个“父母”解析器，然后令单个程序的解析器从该“父母”解析器继承共享选项，这样就不必显式为每个ArgumentParser添加共享选项。
# 第一步是以共享的参数定义建立“父母”解析器。由于“父母”解析器的后代使用者会添加相同的帮助选项，
# 从而会引发一个异常，所以在基础解析器中我们关闭自动帮助选项生成。
import argparse
import argparse_parent

parser  = argparse.ArgumentParser(parents=[argparse_parent.parser])
parser.add_argument('--local-arg', action="store_true", default=False)

print parser.parse_args()