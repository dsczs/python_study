# -*- coding: utf-8 -*-


# 使用opencv操作图像
def t1():
    import numpy as np
    import cv2
    image = cv2.imread("bd_logo1.png", cv2.IMREAD_ANYCOLOR)
    print(image)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 保存图像
    cv2.imwrite('test1.png', image)


# 使用 matplotlib 操作图像
def t2():
    import numpy as np
    import cv2
    from matplotlib import pyplot as plt
    image = cv2.imread("bd_logo1.png", cv2.IMREAD_ANYCOLOR)
    plt.imshow(image, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    t2()
