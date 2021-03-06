# -*- coding:utf-8 -*-
# 截图 抓点用
import pyperclip
import cv2
from core.image import screenshot
import time


def getposBgr(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        x = str(x * 2)
        y = str(y * 2)
        string = "click(" + x + "," + y + ")"
        print(string)
        pyperclip.copy(string)


if __name__ == "__main__":
    #   读 取 图 片
    img = screenshot()  # 直接读为灰度图像
    cv2.imwrite("D:\\PY\\x.jpg", img)
    #   缩小图像10倍(因为我的图片太大，所以要缩小10倍方便显示)
    height, width = img.shape[:2]
    size = (width // 2, height // 2)  # bgr
    img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    # BGR转化为HSV
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 鼠标点击响应事件
    # cv2.imshow("imageHSV",HSV)
    cv2.imshow("get img", img)
    cv2.setMouseCallback("get img", getposBgr)
    time.sleep(0.5)
    cv2.waitKey(0)
