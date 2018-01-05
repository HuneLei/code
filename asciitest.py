# -*- coding: cp936 -*-
from PIL import Image

im = Image.open("两只蓝胖子.jpg")
im.rotate(45).show()