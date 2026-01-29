import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np
from scipy.ndimage import rotate


original_image = Image.open('Flower Color Images Dataset/flowers/flowers/10_011.png')
plt.imshow(original_image)
plt.title("Original Image")
plt.axis('off')
plt.show()

def rotate_image_30_degrees(image):
  return rotate(image, 30, reshape=False)

rotate_img = rotate_image_30_degrees(original_image)
plt.imshow(rotate_img)
plt.title('Rotate Image 30 deg')
plt.axis('off')
plt.show()

horizontal_flip = ImageOps.mirror(original_image)
plt.imshow(horizontal_flip)
plt.title('Horizontal flip')
plt.axis('off')
plt.show()


vertical_flip = ImageOps.flip(horizontal_flip)
plt.imshow(vertical_flip)
plt.title("Mirro + vertical flip")
plt.axis('off')
plt.show()


width, height = original_image.size
new_size = (int(width * 1.2), int(height * 1.2))

zoomed_image = original_image.resize(new_size)

plt.imshow(zoomed_image)
plt.title("Zoom 1.2x")
plt.axis('off')
plt.show()