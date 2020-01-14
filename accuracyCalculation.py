import cv2
import numpy as np
import colour
import os


out = open("./accuracy_output/accuracy.txt", 'w+')

for i in range(int(len([name for name in os.listdir('./deltaE_input')])/5)):

    image1_rgb = cv2.imread("./deltaE_input/" + str(i + 1)+".jpg")
    image2_rgb = cv2.imread("./deltaE_input/batchnorm" + str(i + 1)+".png")
    image3_rgb = cv2.imread("./deltaE_input/spectralnorm" + str(i + 1)+".png")
    image4_rgb = cv2.imread("./deltaE_input/cnn" + str(i + 1)+"-1.png")
    image5_rgb = cv2.imread("./deltaE_input/cnn" + str(i + 1)+"-2.png")

    image1_lab = cv2.cvtColor(image1_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
    image2_lab = cv2.cvtColor(image2_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
    image3_lab = cv2.cvtColor(image3_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
    image4_lab = cv2.cvtColor(image4_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)
    image5_lab = cv2.cvtColor(image5_rgb.astype(np.float32) / 255, cv2.COLOR_RGB2Lab)

    dim = image1_rgb.shape
    height = dim[0]
    width = dim[1]
    channels = dim[2]

    epsilon = .05 #.02

    comp1_matched_pixels = 0
    comp2_matched_pixels = 0
    comp3_matched_pixels = 0
    comp4_matched_pixels = 0

    for x in range(32):
        for y in range(32):
            '''print(str(image1_rgb[x][y][0]) + " -- " + str(image2_rgb[x][y][0]))
            print(str(image1_rgb[x][y][1]) + " -- " + str(image2_rgb[x][y][1]))
            print(str(image1_rgb[x][y][2]) + " -- " + str(image2_rgb[x][y][2]))'''
            if((abs(int(image1_lab[x][y][0]) - int(image2_lab[x][y][0])) < int(image1_lab[x][y][0]*epsilon))
            ):
                comp1_matched_pixels += 1
            if ((abs(int(image1_lab[x][y][0]) - int(image3_lab[x][y][0])) < int(image1_lab[x][y][0] * epsilon))
            ):
                comp2_matched_pixels += 1
            if ((abs(int(image1_lab[x][y][0]) - int(image4_lab[x][y][0])) < int(image1_lab[x][y][0] * epsilon))
            ):
                comp3_matched_pixels += 1
            if ((abs(int(image1_lab[x][y][0]) - int(image5_lab[x][y][0])) < int(image1_lab[x][y][0] * epsilon))
            ):
                comp4_matched_pixels += 1

    #print(comp1_matched_pixels)
    print(100*comp1_matched_pixels/(32*32))
    #print(comp2_matched_pixels)
    print(100 * comp2_matched_pixels / (32 * 32))
    #print(comp3_matched_pixels)
    print(100 * comp3_matched_pixels / (32 * 32))
    #print(comp4_matched_pixels)
    print(100 * comp4_matched_pixels / (32 * 32))
    #print(dim,height,width,channels)


    print("\n -----------------------------")
'''
    and
    (abs(int(image1_rgb[x][y][1]) - int(image2_rgb[x][y][1])) < int(image1_rgb[x][y][1] * epsilon)) and
    (abs(int(image1_rgb[x][y][2]) - int(image2_rgb[x][y][2])) < int(image1_rgb[x][y][2] * epsilon))'''