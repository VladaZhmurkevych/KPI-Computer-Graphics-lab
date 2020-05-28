import scipy.ndimage

def applyMedianFilter(image, size=5):
    imageWithFilter = scipy.ndimage.filters.median_filter(image, size)
    return imageWithFilter

def applyMaximumFilter(image, size=5):
    imageWithFilter = scipy.ndimage.filters.maximum_filter(image, size)
    return imageWithFilter

def applyLaplaceFilter(image):
    imageWithFilter = scipy.ndimage.filters.laplace(image)
    return imageWithFilter

