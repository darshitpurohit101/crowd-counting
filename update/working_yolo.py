# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:19:52 2019

@author: Darshit.Purohit
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:06:31 2019

@author: Darshit.Purohit
"""

import cv2
import matplotlib.pyplot as plt

from utils import load_class_names,  detect_objects, print_objects, plot_boxes
from darknet import Darknet

# Set the location and name of the cfg file
cfgfile = 'D:/HeadCount/YOLO-Object-Detection-master/YOLO-Object-Detection-master/cfg/yolov3.cfg'

# Set the location and name of the pre-trained weights file
weight_file = 'D:/HeadCount/YOLO-Object-Detection-master/YOLO-Object-Detection-master/weights/yolov3.weights'

# Set the location and name of the COCO object classes file
namesfile = 'data/coco.names'

# Load the network architecture
m = Darknet(cfgfile)

# Load the pre-trained weights
m.load_weights(weight_file)
#print("weight")
# Load the COCO object classes
class_names = load_class_names(namesfile)

# Print the neural network used in YOLOv3
m.print_network()


    # Set the default figure 

plt.rcParams['figure.figsize'] = [24.0, 14.0]


# Load the image
img = cv2.imread('Output/trial3.jpg')

# Convert the image to RGB
original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# We resize the image to the input width and height of the first layer of the network.    
resized_image = cv2.resize(original_image, (m.width, m.height))

# Display the images
#plt.subplot(121)
#plt.title('Original Image')
#plt.imshow(original_image)
#plt.subplot(122)
#plt.title('Resized Image')
#plt.imshow(resized_image)
#plt.show()

# Set the NMS threshold
nms_thresh = 0.6

# Set the IOU threshold
iou_thresh = 0.4

print("till here")
# Detect objects in the image
boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)
print("detect_object")
# Print the objects found and the confidence level
print_objects(boxes, class_names)

#Plot the image with bounding boxes and corresponding object class labels
plot_boxes(original_image, boxes, class_names, plot_labels = True)


#https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/