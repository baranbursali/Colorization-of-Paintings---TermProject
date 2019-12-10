import cv2
import numpy as np
import colour

image1_rgb = cv2.imread('1-o.jpg')
image2_rgb = cv2.imread('output.jpg')

image1_lab = cv2.cvtColor(image1_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
image2_lab = cv2.cvtColor(image2_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)


delta_E = colour.delta_E(image1_lab, image2_lab)

"""
hepsi = []
x = 0
for i in image1_lab:
    hepsi.append(colour.delta_E(i,image2_lab[x]))
    x += 1
"""

#print(image2_rgb)
#for i in delta_E:
#    print(i)
print(np.mean(delta_E))


