def convertImageToNegative(image):
    negativeImage = 255 - image
    return negativeImage


def changeImageDarkness(image, coefficient):
    darkerImage = 255.0 * (image / 255.0) ** coefficient
    return darkerImage


