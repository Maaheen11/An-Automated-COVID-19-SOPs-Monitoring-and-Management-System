import numpy as np
import sys
import cv2
from math import pow, sqrt


labels = [line.strip() for line in open('class_labels.txt')]


# Load model
print("\nLoading model...\n")
network = cv2.dnn.readNetFromCaffe('SSD_MobileNet_prototxt.txt', 'SSD_MobileNet.caffemodel')

print("\nStreaming video using device...\n")

code = open("file2.txt", "w")


# Capture video from file or through device
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while cap.isOpened():

    # Capture one frame after another
    _, frame = cap.read()

    (h, w) = frame.shape[:2]

    # Resize the frame to suite the model requirements. Resize the frame to 300X300 pixels
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

    network.setInput(blob)
    detections = network.forward()

    pos_dict = dict()
    coordinates = dict()

    for i in range(detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:

            class_id = int(detections[0, 0, i, 1])

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')

            # Filtering only persons detected in the frame. Class Id of 'person' is 15
            if class_id == 15.00:

                # Draw bounding box for the object
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0,0,255), 2)

                label = "{}: {:.2f}%".format(labels[class_id], confidence * 100)

                coordinates[i] = (startX, startY, endX, endY)

                # Mid point of bounding box
                x_mid = round((startX+endX)/2,4)
                y_mid = round((startY+endY)/2,4)


                pos_dict[i] = (x_mid,y_mid)

    # Distance between every object detected in a frame
    close_objects = set()
    for i in pos_dict.keys():
        for j in pos_dict.keys():
            if i < j:
                dist = sqrt(pow(pos_dict[i][0]-pos_dict[j][0],2) + pow(pos_dict[i][1]-pos_dict[j][1],2) )

                if dist < 1200:
                    close_objects.add(i)
                    close_objects.add(j)

    for i in pos_dict.keys():
        (startX, startY, endX, endY) = coordinates[i]
        if i in close_objects:
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0,0,255), 2)
            code.seek(0)
            code.write("3")
        else:
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0,255,0), 2)
            code.seek(0)
            code.write("5")
        

            

    # Show frame
    frame2 = cv2.resize(frame,(640, 480))
    cv2.imshow('Social Distancing Detector', frame2)


    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
