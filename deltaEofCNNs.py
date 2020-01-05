import cv2
import numpy as np
import colour
import os

out = open("./deltaE_output/output.txt", 'w+')

for i in range(int(len([name for name in os.listdir('./deltaE_input')])/5)):

    image1_rgb = cv2.imread("./deltaE_input/" + str(i + 1)+".jpg")
    image2_rgb = cv2.imread("./deltaE_input/cnn" + str(i + 1)+"-1.png")
    image3_rgb = cv2.imread("./deltaE_input/cnn" + str(i + 1)+"-2.png")

    image1_lab = cv2.cvtColor(image1_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
    image2_lab = cv2.cvtColor(image2_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
    image3_lab = cv2.cvtColor(image3_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)

    delta_E_1 = colour.delta_E(image1_lab, image2_lab)
    delta_E_2 = colour.delta_E(image1_lab, image3_lab)

    cnn1 = str(i + 1) + " - " + str(np.mean(delta_E_1))
    cnn2 = str(np.mean(delta_E_2))
    out.write(cnn1 + " " + cnn2 + "\n")




