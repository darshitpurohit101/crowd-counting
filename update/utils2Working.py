import time
import torch
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import notification
import consider
import dataentry
import queueDetect
import centroids_tracker
import tracker

def boxes_iou(box1, box2):

    # Get the Width and Height of each bounding box
    width_box1 = box1[2]
    height_box1 = box1[3]
#    print(width_box1, height_box1)
    width_box2 = box2[2]
    height_box2 = box2[3]
    
    # Calculate the area of the each bounding box
    area_box1 = width_box1 * height_box1
    area_box2 = width_box2 * height_box2
    
    # Find the vertical edges of the union of the two bounding boxes
    mx = min(box1[0] - width_box1/2.0, box2[0] - width_box2/2.0)
    Mx = max(box1[0] + width_box1/2.0, box2[0] + width_box2/2.0)
    
    # Calculate the width of the union of the two bounding boxes
    union_width = Mx - mx
    
    # Find the horizontal edges of the union of the two bounding boxes
    my = min(box1[1] - height_box1/2.0, box2[1] - height_box2/2.0)
    My = max(box1[1] + height_box1/2.0, box2[1] + height_box2/2.0)    
    
    # Calculate the height of the union of the two bounding boxes
    union_height = My - my
    
    # Calculate the width and height of the area of intersection of the two bounding boxes
    intersection_width = width_box1 + width_box2 - union_width
    intersection_height = height_box1 + height_box2 - union_height
   
    # If the the boxes don't overlap then their IOU is zero
    if intersection_width <= 0 or intersection_height <= 0:
        return 0.0

    # Calculate the area of intersection of the two bounding boxes
    intersection_area = intersection_width * intersection_height
    
    # Calculate the area of the union of the two bounding boxes
    union_area = area_box1 + area_box2 - intersection_area
    
    # Calculate the IOU
    iou = intersection_area/union_area
    
    return iou


def nms(boxes, iou_thresh):
    
    # If there are no bounding boxes do nothing
    if len(boxes) == 0:
        return boxes
    
    # Create a PyTorch Tensor to keep track of the detection confidence
    # of each predicted bounding box
    det_confs = torch.zeros(len(boxes))
    
    # Get the detection confidence of each predicted bounding box
    for i in range(len(boxes)):
        det_confs[i] = boxes[i][4]

    # Sort the indices of the bounding boxes by detection confidence value in descending order.
    # We ignore the first returned element since we are only interested in the sorted indices
    _,sortIds = torch.sort(det_confs, descending = True)
    
    # Create an empty list to hold the best bounding boxes after
    # Non-Maximal Suppression (NMS) is performed
    best_boxes = []
    
    # Perform Non-Maximal Suppression 
    for i in range(len(boxes)):
        
        # Get the bounding box with the highest detection confidence first
        box_i = boxes[sortIds[i]]
        
        # Check that the detection confidence is not zero
        if box_i[4] > 0:
            
            # Save the bounding box 
            best_boxes.append(box_i)
            
            # Go through the rest of the bounding boxes in the list and calculate their IOU with
            # respect to the previous selected box_i. 
            for j in range(i + 1, len(boxes)):
                box_j = boxes[sortIds[j]]
                
                # If the IOU of box_i and box_j is higher than the given IOU threshold set
                # box_j's detection confidence to zero. 
                if boxes_iou(box_i, box_j) > iou_thresh:
                    box_j[4] = 0
                    
    return best_boxes


def detect_objects(model, img, iou_thresh, nms_thresh):
    
    # Start the time. This is done to calculate how long the detection takes.
    start = time.time()
    
    # Set the model to evaluation mode.
    model.eval()
    
    # Convert the image from a NumPy ndarray to a PyTorch Tensor of the correct shape.
    # The image is transposed, then converted to a FloatTensor of dtype float32, then
    # Normalized to values between 0 and 1, and finally unsqueezed to have the correct
    # shape of 1 x 3 x 416 x 416
    img = torch.from_numpy(img.transpose(2,0,1)).float().div(255.0).unsqueeze(0)
    
    # Feed the image to the neural network with the corresponding NMS threshold.
    # The first step in NMS is to remove all bounding boxes that have a very low
    # probability of detection. All predicted bounding boxes with a value less than
    # the given NMS threshold will be removed.
    list_boxes = model(img, nms_thresh)
    
    # Make a new list with all the bounding boxes returned by the neural network
    boxes = list_boxes[0][0] + list_boxes[1][0] + list_boxes[2][0]
    
    # Perform the second step of NMS on the bounding boxes returned by the neural network.
    # In this step, we only keep the best bounding boxes by eliminating all the bounding boxes
    # whose IOU value is higher than the given IOU threshold
    boxes = nms(boxes, iou_thresh)
    
    # Stop the time. 
    finish = time.time()
    
    # Print the time it took to detect objects
    print('\n\nIt took {:.3f}'.format(finish - start), 'seconds to detect the objects in the image.\n')
    
    # Print the number of objects detected
#    print('Number of object Detected:', len(boxes), '\n')
    
    return boxes


def load_class_names(namesfile):
    # Create an empty list to hold the object classes
    class_names = []
    
    # Open the file containing the COCO object classes in read-only mode
    with open(namesfile, 'r') as fp:
        
        # The coco.names file contains only one object class per line.
        # Read the file line by line and save all the lines in a list.
        lines = fp.readlines()
    
    # Get the object class names
    for line in lines:
        
        # Make a copy of each line with any trailing whitespace removed
        line = line.rstrip()
        
        # Save the object class name into class_names
        class_names.append(line)
        
    return class_names

def plot_boxes(i, frame_no, img, boxes, class_names, r, plot_labels = True, color = None):
    queue_counter = 0  
    rect_lst = []
    frame_no = frame_no
    # Define a tensor used to set the colors of the bounding boxes
    colors = torch.FloatTensor([[1,0,1],[0,0,1],[0,1,1],[0,1,0],[1,1,0],[1,0,0]])
    
    # Define a function to set the colors of the bounding boxes
    def get_color(c, x, max_val):
        ratio = float(x) / max_val * 5
        i = int(np.floor(ratio))
        j = int(np.ceil(ratio))
        
        ratio = ratio - i
        r = (1 - ratio) * colors[i][c] + ratio * colors[j][c]
        
        return int(r * 255)
    
    # Get the width and height of the image
    width = img.shape[1]
    height = img.shape[0]
    

#    cv2.imwrite('D:\HeadCount\YOLO-Object-Detection-master\YOLO-Object-Detection-master\Output\out' +str(frame_no)+'.jpeg', img)
    
    # Plot the bounding boxes and corresponding labels on top of the image
    for i in range(len(boxes)):
        rects = []
   
        # Get the ith bounding box
        box = boxes[i]
        c = box[6]
        if class_names[c] == 'person':
#            print('true: ',class_names[c])
            # Get the (x,y) pixel coordinates of the lower-left and lower-right corners
            # of the bounding box relative to the size of the image.
            nx = int(np.around((box[0] - box[1]/2.0) * width))
            ny = int(np.around((box[2] - box[3]/2.0) * width))
            x1 = int(np.around((box[0] - box[2]/2.0) * width))
            y1 = int(np.around((box[1] - box[3]/2.0) * height))
            x2 = int(np.around((box[0] + box[2]/2.0) * width))
            y2 = int(np.around((box[1] + box[3]/2.0) * height))
            
            # Set the default rgb value to red
            rgb = (1, 0, 0)
                
            # Use the same color to plot the bounding boxes of the same object class
            if len(box) >= 7 and class_names:
                cls_conf = box[5]
                cls_id = box[6]
                classes = len(class_names)
                offset = cls_id * 123457 % classes
                red   = get_color(2, offset, classes) / 255
                green = get_color(1, offset, classes) / 255
                blue  = get_color(0, offset, classes) / 255
                
                # If a color is given then set rgb to the given color instead
                if color is None:
                    rgb = (red, green, blue)
                else:
                    rgb = color
            
            # Calculate the width and height of the bounding box relative to the size of the image.
            width_x = x2 - x1
    #        width_y = y1 - y2
            width_y = -200
            
            x = int((x1+x2)/2)
            y = int((y1+y2)/2)
            
            check_point = consider.check(r[0][0],r[0][1], r[1][0], r[0][1], r[1][0],r[1][1],  
                    r[0][0],r[1][1], x, y) # 99%
#            check_point = 1
            shape = np.array([[[r[0][0],r[0][1]], [r[1][0], r[0][1]], [r[1][0],r[1][1]], [r[0][0],r[1][1]]]], np.int32)
#            shape = np.array([[r]], np.int32)
#            points = shape.reshape((-1, 1, 2))
            img = cv2.polylines(img, [shape], True, (0,200,255),5)
#            img = cv2.line(img, r[0], r[1], (0,255,255), 2)
            
            if check_point == 1: #.....................
#                print(x1,y1," ",x2,y2)
                queue_counter += 1
                rect_lst.append([x,y])
                img = cv2.line(img, (x, y1), (x, y2), (255,0,0), 2)
                img = cv2.circle(img,(x,y), 5, (0,0,255), 1)
                org = (x,y)
                font = cv2.FONT_HERSHEY_SIMPLEX 
                fontScale = 0.5
                color = (0, 255, 0) 
                thickness = 2
                txt = str(x)+','+str(y)
                cv2.putText(img, txt, org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
#                cv2.imshow('cent',img)
#                cv2.waitKey(0)
#                img = cv2.rectangle(img, (x1, y1, width_x, width_y), (0,255,0), 1)
    rect_lst = sorted(rect_lst)
    print('list',rect_lst)
    r = queueDetect.Detect()
    r.key_values(rect_lst)
#    print(p)
    print('person standing in queue: ',queue_counter)
    framename = 'output' + str(frame_no)
#    dataentry.datawrite(framename, queue_counter)
#    plt.savefig('D:\Queue Managment v1\Output\out' +str(frame_no)+'.png')
#    im = cv2.imread('D:\Queue Managment v1\Output\out' +str(frame_no)+'.png')
#    imS = cv2.resize(im, (800,700))
    cv2.imwrite('Output/'+str(framename)+'.jpg',img)
    cv2.imshow('draw',img)
#    plt.show()
#    cv2.imwrite('Output/Output{}'.format(framename), img)
    cv2.waitKey(2)
    
#    plt.show()
