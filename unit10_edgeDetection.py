import cv2

def sobelEdgeDetection(image, asix='x', ksize=5):
    img = cv2.imread(image, 0)
    dx, dy = [1, 0] if asix == 'x' else [0, 1]
    resultImage = cv2.Sobel(img, -1, dx, dy, ksize)
    return resultImage
