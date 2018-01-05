import argparse

parser = argparse.ArgumentParser(description='Change the option prefix charaters',
                                 prefix_chars='-+/')

parser.add_argument('-a', action="store_false", default=None,
                    help='Turn A off')

parser.add_argument('+a', action="store_true", default=None,
                    help='Turn A on')

parser.add_argument('//noarg', '++noarg', action="store_true", default=False)

print parser.parse_args()

# $ python argparse_prefix_chars.py -h
#
# usage: argparse_prefix_chars.py [-h] [-a] [+a] [//noarg]
#
# Change the option prefix characters
#
# optional arguments
#     -h, --help  show this help message and exit
#     -a  Turn A off
#     +a  Turn A on
#     //noarg,++noarg
#
# $ python argparse_prefix_chars.py +a
#
# Namespace(a=True, noarg=False)
#
# $ python argparse_prefix_chars.py -a
#
# Namespace(a=False, noarg=False)
#
# $ python argparse_prefix_chars.py //noarg
#
# Namespace(a=None, noarg=True)
#
# $ python argparse_prefix_chars.py ++noarg
#
# Namespace(a=None, noarg=True)
#
# $ python argparse_prefix_chars.py --noarg
#
# usage: argparse_prefix_chars.py [-h] [-a] [+a] [//noarg]
# argparse_prefix_chars.py: error: unrecognized arguments: --noarg
