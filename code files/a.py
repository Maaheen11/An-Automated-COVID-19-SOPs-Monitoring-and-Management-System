import cv2
import tensorflow as tf
import mediapipe as mp
import numpy as np
import time
from tensorflow import keras
from tensorflow.keras.preprocessing import image



# Webcam
capture = cv2.VideoCapture(0)
#capture.set(3, 640)		# 320x240
#capture.set(4, 360)

# FPS
pTime = 0
cTime = 0

interpreter = tf.lite.Interpreter(model_path = "./model.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]


mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


code = open("file.txt", "w")

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
  while True:
    isTrue, frame = capture.read()      # Capture frame by frame
    results = face_detection.process(frame)
    if results.detections:
      for detection in results.detections:
        coordinates = detection.location_data.relative_bounding_box
        h, w, c = frame.shape
        xmin= int(coordinates.xmin * w)
        ymin = int(coordinates.ymin * h)
        height = int(coordinates.height * h)
        width = int(coordinates.width * w)

        xmax = xmin + width
        ymax = ymin + height

        img_input = frame[ymin-60:ymax+45, xmin-40:xmax+40]

        try:
          cv2.imwrite("./i.jpg", img_input)
          path = "./i.jpg"
          img = image.load_img(path, target_size=(100, 100))
        except Exception:
          continue


        x = image.img_to_array(img)
        x = x / 255.0
        x = np.expand_dims(x, axis=0)

        interpreter.set_tensor(input_index, x)
        interpreter.invoke()
        classes = interpreter.get_tensor(output_index)

        print(classes[0])

        if classes[0] > 0.5:
          cv2.putText(frame, "No Mask Detected", (xmin, ymin -4), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
          cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
          code.seek(0)
          code.write("2")
        else:
          cv2.putText(frame, "Mask Detected", (xmin, ymin - 4), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
          cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (255, 255, 255), 2)
          code.seek(0)
          code.write("9")

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (18, 75), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)
    #frame = cv2.resize(frame, (1080, 720))
    cv2.imshow('Detection', frame)
    if cv2.waitKey(5) & 0xFF == 27:
      break

capture.release()
cv2.destroyAllWindows()
code.close()

