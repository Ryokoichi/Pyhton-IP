import cv2
import numpy as np
import functions as fcn
from pathlib import Path
import os


folder = os.listdir('/Original')
files = [x for x in folder if x.endswith(".png")]

print(files)

for file in files:
    path = r'Original\\' + file
    img = cv2.imread(path)
    img = fcn.reSize(img, 200)
    org = img
    org = fcn.AddPadding(org, 10)
    cv2.imshow('ORG', org)
    imgB = cv2.GaussianBlur(img, (5, 5), 0)
    opening = fcn.Thresholds(imgB)

    contours, hierarchy = cv2.findContours(
        opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cntrs = cv2.drawContours(org, contours, -1, (0, 255, 0), 2)

    imgB = fcn.AddPadding(imgB, 10)
    img = fcn.AddPadding(img, 10)
    i = 1
    for contour in contours:
        M = cv2.moments(contour)
        area = cv2.contourArea(contour)
        if area > 300 and area < 5000:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            # circle = cv2.circle(imgB, center, radius, (0, 255, 0), 2)
            #fcn.AddText(imgB, str(area), x, y)
             # cv2.imshow('circles', circle)
            tolarance = 20
            cirlce_x1 = int(x - radius) - tolarance
            cirlce_y1 = int(y - radius) - tolarance
            cirlce_x2 = int(x + radius) 
            cirlce_y2 = int(y + radius) 
            #print(str(cirlce_x1) + '\t' + str(cirlce_y1) + '\t' + str(cirlce_x2) + '\t' + str(cirlce_y2))
            # coreFolder = '\\Outputs\\Cores\\' + file.replace('.png', '')
            # if not os.path.exists(coreFolder):
            #     os.makedirs(coreFolder)
           
            i = i + 1
            #cv2.imshow('contours', cntrs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('Cores created in ' + file)




