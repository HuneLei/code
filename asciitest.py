# -*- coding: cp936 -*-
from PIL import Image

im = Image.open("��ֻ������.jpg")
im.rotate(45).show()