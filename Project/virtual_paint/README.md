# Little description of how it works
1. Webcam takes the video(set on frames and each frame can be refered as image)
2. Webcam each frames(images)is converted in HSV format (Hue, Saturation, Value) 
   so that we can find the mask of the required color.
3. Mask is feeded to the contours funtion so that we can get the shape of the mask
   and find the centre point of the shape.
4. Now, here we are talking about video that means set of frames(images) so we will
   get different centre point for each image we will store all the points in list.
5. This list will be feed to drawOnCanvas function so we can draw circle on each point
   in the list.
