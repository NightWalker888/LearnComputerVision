from email import header


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件:image_filter.py
@说明:
@时间:2022/01/29 20:42:50
@作者:NighWalker888
@版本:1.0
'''

import cv2 
import logging
logging.basicConfig(level = logging.DEBUG)

if __name__ == "__main__":
    img_pth = "../demo_images/cat.jpg"
    img = cv2.imread(img_pth)
    print(img.shape)

