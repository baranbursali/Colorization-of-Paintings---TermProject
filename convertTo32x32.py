import os
import cv2

counter = 0
for i in os.listdir('./imgs'):
    img = cv2.imread("./imgs/"+str(i))
    img = cv2.resize(img, (32,32))
    #cv2.imshow("name",img)


    #cv2.waitKey(0)  # waits until a key is pressed

    cv2.imwrite('./out_imgs/' + str(counter) + ".jpg", img)
    counter += 1