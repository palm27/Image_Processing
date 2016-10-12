import cv2
import numpy as np



#Liews Wuttipat

#Input Image

#Image Enchancement
# -- Sharp, Blur

#Image Morphological Processing
# -- Erod

#Image Segmentation
# --

#Feature Extraction
# -- Properties of Shape, Area, Length
# -- SIFT Feature
# -- HOG Feature

#Classification
# -- SVM Support Vector Machine
# -- Neuron Network
# -- AdaBoost

#Output Image

img = cv2.imread('image.png')
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.bitwise_not(cv2.threshold(img_grey, 127, 255, 0)[1])

#cv2.CHAIN_APPROX_NONE   ### Draw all of contour
#cv2.CHAIN_APPROX_SIMPLE ### Draw only critical point

_, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    #Find moments and find center of mass
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01']/M['m00'])

    #Approximation shape from arclength 3%
    epsilon = 0.03 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)


    #Draw approx
    for i in approx:
        cv2.circle(img, (i[0][0], i[0][1]), 3, (255, 0, 0), -1)

    #Draw center of mass
    cv2.circle(img, (cx, cy), 3, (0, 255, 0), -1)

    #Draw text on Image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, '('+str(cx)+', '+str(cy)+')', (cx-20, cy+35), font, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
    txt = ''
    if len(approx)==3:
        txt = 'Triangle'
    elif len(approx)==4:
        txt = 'Rectangle'
    elif len(approx)==8:
        txt = 'Circle'
    cv2.putText(img, txt, (cx - 20, cy + 55), font, 0.4, (0, 0, 255), 1,cv2.LINE_AA)

cv2.imshow('Output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

