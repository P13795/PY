# -*- coding:utf-8 -*-
from image import compare_image, cut_image
from sub import get_img
import numpy as np


def search(y0: int, y1: int, x0: int, x1: int, img1, img2, value: float):
    """通用图像对比

    Args:
        y0,y1,x0,x1 (int): 对比区域四角坐标
        img1 (memoryview/get_img): 被裁剪的图
        img2 (memoryview): 被对比的图
        value (float): 相似度

    Returns:
        [bool]: [符合返回真，不符合返回假]
    """
    if img1 is get_img:
        cut_img = cut_image(y0, y1, x0, x1, img1())
    else:
        cut_img = cut_image(y0, y1, x0, x1, img1)
    if isinstance(img2, np.ndarray):
        x = compare_image(cut_img, img2)
        if x >= value:
            return True
        else:
            return False
    if isinstance(img2, tuple):
        x = []
        for img in img2:
            x.append(compare_image(cut_img, img))
        if max(x) >= value:
            return x.index(max(x))
        else:
            return False
