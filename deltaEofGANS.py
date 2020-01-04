import cv2
import numpy as np
import colour
import os

out = open("./deltaE_output_GANS/output.txt", 'w')

for i in range(int(len([name for name in os.listdir('./deltaE_input')])/5)):

    image1_rgb = cv2.imread("./deltaE_input/" + str(i + 1)+".jpg")
    image2_rgb = cv2.imread("./deltaE_input/batchnorm" + str(i + 1)+".png")
    image3_rgb = cv2.imread("./deltaE_input/spectralnorm" + str(i + 1)+".png")

    image1_lab = cv2.cvtColor(image1_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
    image2_lab = cv2.cvtColor(image2_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
    image3_lab = cv2.cvtColor(image3_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)

    delta_E_batchnorm = colour.delta_E(image1_lab, image2_lab)
    delta_E_spectralnorm = colour.delta_E(image1_lab, image3_lab)

    meanBatch = str(i + 1) + " - " + str(np.mean(delta_E_batchnorm))
    meanSpectral = str(np.mean(delta_E_spectralnorm))
    out.write(meanBatch + " " + meanSpectral + "\n")




