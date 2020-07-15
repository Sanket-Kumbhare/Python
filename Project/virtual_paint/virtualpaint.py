# Imported required libraries
import cv2 as cv
import numpy as np


# Webcamp setup
cap = cv.VideoCapture(0)
cap.set(3, 640) #For width of output window
cap.set(4, 480) #For height of output window


# Making mask
def mask(img):
    newpoints = [] # Empty list for appending the points traced by the contours function
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) # Converting normal captured image to the HSV 
    lower = np.array([0, 153, 200]) # Lower value of Hue, Saturation, Value respectively
    upper = np.array([179, 255, 255]) # Upper value of Hue, Saturation, Value respectively

    # Masking the required orange color using lower and upper values of Hue, Saturation, Value
    mask = cv.inRange(hsv, lower, upper) 

    # Contours function is called so that we get the centre point of the mask 
    x, y = getContours(mask) 

    # Drawing a circle on the centre of the mask we get by calling Contours function
    cv.circle(imgresult, (x, y), 7, (51, 153, 255), cv.FILLED) 

    # Checking for if the webcam is not able to detect the centre point of the required mask then don't add to the newpoint list
    if x != 0 and y != 0 : 
        newpoints.append([x,y])
    return newpoints


# Contours funtion
def getContours(img):

    # Get the contours from the image
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    x, y, w, h = 0, 0, 0, 0 # Default values for x, y, height and width respectively

    # Since video are made by frames and each frame is an image so we have to run a loop for getting centre point of the required mask
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500 :
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02* peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return x + w // 2, y + h // 2


mypoints = [] # Empty list for storing the newpoints which has to be filled by color


# This function draw circle for each new point 
def drawOnCanvas(mypoints):
    for point in mypoints:
        cv.circle(imgresult, (point[0], point[1]), 7, (51, 153, 255), cv.FILLED)


# Webcam loop
while True:
    success, image = cap.read() # Success values stores the boolean value True and image variable stores the image array of frame
    img = cv.flip(image, 1) # Webcam shows us the mirror image so we have to flip it
    imgresult = img.copy() # Copying the image and storing in another variable 
    newpoint = mask(img) # Calling mask function and list of traced point by the mask

    # Checking for the newpoint list is not empty if it is empty that means orange color is not detected and Running loop for newpoint list and appending each newpoint to the mypoint list so that we can pass it to the drawOnCanvas funtion for drawing color on each newpoint  
    if newpoint != 0 :
        for newp in newpoint:
            mypoints.append(newp)

    # Checking for the newpoint list is not empty if it is empty that means orange color is not detected and don't draw any circle
    if len(mypoints) != 0:
        drawOnCanvas(mypoints)
    cv.imshow("result", imgresult) # Show the output

    # This check closes the output window if we click 'q' key
    if cv.waitKey(1) == ord("q"):
        break