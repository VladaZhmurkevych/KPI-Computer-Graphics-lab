import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import unit8_grayLeveltransformation as grayLevel
import unit9_neighborhoodProcessing as neighborhood
import unit10_edgeDetection as edgeDetection

imageName = 'apple.jpg'

image = np.array(Image.open(imageName).convert('L'))

negativeImage = grayLevel.convertImageToNegative(image)
darkerImage = grayLevel.changeImageDarkness(image, 2)

imageWithMedianFilter = neighborhood.applyMedianFilter(image)
imageWithMaximumFilter = neighborhood.applyMaximumFilter(image)
imageWithLaplaceFilter = neighborhood.applyLaplaceFilter(image)

imageWithSobelEdgeDetection = edgeDetection.sobelEdgeDetection(imageName)

plt.figure(figsize=(30, 30))

plt.subplot(2, 4, 1)
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.title('Original Image')

plt.subplot(2, 4, 2)
plt.imshow(negativeImage, cmap='gray', vmin=0, vmax=255)
plt.title('Negative Image')

plt.subplot(2, 4, 3)
plt.imshow(darkerImage, cmap='gray', vmin=0, vmax=255)
plt.title('Darker Image')

plt.subplot(2, 4, 4)
plt.imshow(imageWithMedianFilter, cmap='gray', vmin=0, vmax=255)
plt.title('Image With Median Filter')

plt.subplot(2, 4, 5)
plt.imshow(imageWithMaximumFilter, cmap='gray', vmin=0, vmax=255)
plt.title('Image With Maximum Filter')

plt.subplot(2, 4, 6)
plt.imshow(imageWithLaplaceFilter, cmap='gray', vmin=0, vmax=255)
plt.title('Image With Laplace Filter')

plt.subplot(2, 4, 7)
plt.imshow(imageWithSobelEdgeDetection, cmap='gray', vmin=0, vmax=255)
plt.title('Image With Sobel Edge Detection')

plt.show()
