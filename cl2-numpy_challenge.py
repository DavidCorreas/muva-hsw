import numpy as np
from PIL import Image

b = (23, 58)
g = (34, 200)
r = (2, 35)
pil_image = Image.open('data/numpy-challenge/chroma.png')

input_image = np.asarray(pil_image)
size = input_image.shape
output_mask_bad = np.zeros(size[:- 1], np.uint8)

for x in range(size[0]):
    for y in range(size[1]):
        in_range_b = b[0] <= input_image[x, y, 2] < b[1]
        in_range_g = g[0] <= input_image[x, y, 1] < g[1]
        in_range_r = r[0] <= input_image[x, y, 0] < r[1]
        output_mask_bad[x, y] = in_range_b and in_range_g and in_range_r

# SOLUCION
red_mask = (r[1] >= input_image[:, :, 0]) & (input_image[:, :, 0] >= r[0])
green_mask = (g[1] >= input_image[:, :, 1]) & (input_image[:, :, 1] >= g[0])
blue_mask = (b[1] >= input_image[:, :, 2]) & (input_image[:, :, 2] >= b[0])
output_mask = (red_mask & green_mask & blue_mask) * 1

# COMPROBACION
np_equals = (output_mask == output_mask_bad).all()
