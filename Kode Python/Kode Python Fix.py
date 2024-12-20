import serial
import time
from ultralytics import YOLO
import cv2
import math
import serial.tools.list_ports
import urllib.request
import numpy as np

serialcomm = serial.Serial('COM6', 115200)
serialcomm.timeout = 1
url = 'http://192.168.1.6/cam-hi.jpg'

# cap=cv2.VideoCapture(0)

# frame_width=int(cap.get(3))
# frame_height = int(cap.get(4))


model=YOLO("best.pt")
classNames = ["Person"]

while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    results=model(img,stream=True)
    for r in results:
        boxes=r.boxes
        nomer=r.__len__()
        if nomer==0:
            command = str("False.")
        if nomer > 0:
            command = str("True.")
        print(command)
        serialcomm.write(command.encode())
        time.sleep(0.5)
        print(serialcomm.readline().decode('ascii'))
        
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            #print(x1, y1, x2, y2)
            x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
            print(x1,y1,x2,y2)
            cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,255),3)
            #print(box.conf[0])
            conf=math.ceil((box.conf[0]*100))/100
            cls=int(box.cls[0])
            class_name=classNames[cls]
            label=f'{class_name}{conf}'
            t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
            #print(t_size)
            c2 = x1 + t_size[0], y1 - t_size[1] - 3
            cv2.rectangle(img, (x1,y1), c2, [255,0,255], -1, cv2.LINE_AA)  # filled
            cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)
            
    
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF==ord('1'):
        break
    
serialcomm.close()