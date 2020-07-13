import cv2
import numpy as np

def empty(a):                                      #This will do nothing
    pass


image = cv2.imread('E:\chirag\my project file\images for cv\human face.jpg')
HSVimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640,240)
cv2.createTrackbar('Hue min', 'TrackBar', 0,179, empty)      #hue min is the first value we need to change,
                                                             # the hue value in cv2 ranges till 180(0,179)
cv2.createTrackbar('Hue max', 'TrackBar', 179,179, empty)    #'empty' function is created which does nothing because createTrackbar needs a function name to be passed 
cv2.createTrackbar('Sat min', 'TrackBar', 0,255, empty)
cv2.createTrackbar('Sat max', 'TrackBar', 255,255, empty)
cv2.createTrackbar('Val min', 'TrackBar', 0,255, empty)
cv2.createTrackbar('Val max', 'TrackBar', 255,255, empty)

while True:
    h_min = cv2.getTrackbarPos('Hue min','TrackBar')      #senses the tracker position 
    h_max = cv2.getTrackbarPos('Hue max','TrackBar')
    s_min = cv2.getTrackbarPos('Sat min','TrackBar')
    s_max = cv2.getTrackbarPos('Sat max','TrackBar')
    v_min = cv2.getTrackbarPos('Val min','TrackBar')
    v_max = cv2.getTrackbarPos('Val max','TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)      #prints the sensed tracker position in a loop and prints whenever we change the tracker
    lower = np.array([h_min,s_min,v_min],np.uint8)
    upper = np.array([h_max,s_max,v_max],np.uint8)
    mask = cv2.inRange(HSVimage, lower, upper)
    imgresult = cv2.bitwise_and(image,HSVimage,mask=mask)  #bitwise_and will check the pixels in both images and where the
                                                        #pixel matches it will show the color
    mask_inv = cv2.bitwise_not(mask)                    #this is inverse of masked image


    cv2.imshow('original', image)
    # cv2.imshow('HSV image', HSVimage)
    cv2.imshow('mask', mask)
    cv2.imshow('mask inverse', mask_inv)
    cv2.imshow('result', imgresult)
    cv2.waitKey(1)
