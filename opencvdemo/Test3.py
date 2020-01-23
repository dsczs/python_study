# -*- coding: utf-8 -*-


def zh_ch(string):
    return string.encode("gbk").decode(errors="ignore")


# draw line
def t1():
    import numpy as np
    import cv2
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 2)
    cv2.imshow(zh_ch("直线"), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# draw rectangle
def t2():
    import numpy as np
    import cv2
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.rectangle(img, (0, 0), (444, 444), (255, 255, 0), 2)
    cv2.imshow("rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# draw cycle
def t3():
    import numpy as np
    import cv2
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.circle(img, (222, 222), 150, (255, 255, 0), 2)
    cv2.imshow("cycle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    t3()
