import cv2
import numpy as np
import colour
import os

out = open("./deltaE_output_GANS/output.txt", 'w')

batches = []
spects = []

for i in range(int(len([name for name in os.listdir('./deltaE_input')])/3)):

    image1_rgb = cv2.imread("./deltaE_input/" + str(i )+".jpg")
    image2_rgb = cv2.imread("./deltaE_input/batchnorm" + str(i)+".png")
    image3_rgb = cv2.imread("./deltaE_input/spectralnorm" + str(i)+".png")

    image1_lab = cv2.cvtColor(image1_rgb.astype(np.float32) / 255, cv2.COLOR_BGR2LAB)
    image2_lab = cv2.cvtColor(image2_rgb.astype(np.float32) / 255, cv2.COLOR_BGR2LAB)
    image3_lab = cv2.cvtColor(image3_rgb.astype(np.float32) / 255, cv2.COLOR_BGR2LAB)

    delta_E_batchnorm = colour.delta_E(image1_lab, image2_lab)
    delta_E_spectralnorm = colour.delta_E(image1_lab, image3_lab)

    meanBatch = str(i) + " - " + str(np.mean(delta_E_batchnorm))
    meanSpectral = str(np.mean(delta_E_spectralnorm))

    batches.append(delta_E_batchnorm)
    spects.append(delta_E_spectralnorm)

    out.write(meanBatch + " " + meanSpectral + "\n")

print(np.mean(batches))
print(np.mean(spects))


