# -*- coding: cp936 -*-
import argparse
# ���¼�ʾ������3����ͬ��ѡ�һ������ѡ�-a����һ���򵥵��ַ���ѡ�-b�����Լ�һ������ѡ�-c����
parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print parser.parse_args(['-a', '-bval', '-c', '3'])

# ������ѡ�����֣���ѡ������ֶ���һ���ַ�������ͬ�ķ�ʽ���д���
parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--noarg', action="store_true", default=False)
parser.add_argument('--witharg', action="store", dest="witharg")
parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)

print parser.parse_args(['--noarg', '--witharg', 'val', '--witharg2=3'])

# ����������У���count��������һ����������units�������洢Ϊһ���ַ�������������һ��������û�������������ṩ���������ֵ���ܱ�ת��Ϊ��ȷ�����ͣ��ͻᱨ��һ������
parser = argparse.ArgumentParser(description='Example with non-optional arguments')

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print parser.parse_args()