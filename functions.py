import cv2
import numpy as np

def AddText(img, text, x, y):
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText =  (int(x), int(y))
        fontScale              = 0.5
        fontColor              = (0,0,255)
        lineType               = 1

        cv2.putText(img, text, 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,
            lineType)
        

def reSize(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def AddPadding(im, bordersize):
    row, col = im.shape[:2]
    bottom = im[row-2:row, 0:col]
    mean = cv2.mean(bottom)[0]

   
    white = [255,255,255]
    return cv2.copyMakeBorder(
        im,
        top=bordersize,
        bottom=bordersize,
        left=bordersize,
        right=bordersize,
        borderType=cv2.BORDER_CONSTANT,
        value=white
    )
    
    
def Thresholds(imgB):
    # cv2.fastNlMeansDenoisingColored(img, None, 2, 2, 7, 21)
    
    imgB = AddPadding(imgB, 10)

    gray = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

    image_enhanced = cv2.equalizeHist(gray)
    #cv2.imshow('image_enhanced', image_enhanced)

    ret, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
    #ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thresh = AddPadding(thresh, 10)

    #cv2.imshow('thresh', thresh)

    kernel = np.ones((1, 1), np.uint8)
    erosion = cv2.dilate(thresh, kernel, iterations=20)
    #cv2.imshow('erosion', erosion)

    kernel = np.ones((2, 2), np.uint8)
    opening = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel, iterations=4)
    return opening
    #cv2.imshow('opening', opening)