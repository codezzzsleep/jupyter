import cv2


def stretch(img):
    '''
    图像拉伸函数
    '''
    maxi = float(img.max())
    mini = float(img.min())

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = (255 / (maxi - mini) * img[i, j] - (255 * mini) / (maxi - mini))

    return img


if __name__ == '__main__':
    img = cv2.imread('car.jpg')
    cv2.imshow("img", img)
    stretch_img = stretch(img)
    cv2.imshow("stretch_img", stretch_img)
    cv2.waitKey(0)
