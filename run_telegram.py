import torch
import cv2
import requests
import time

model = torch.hub.load('', 'custom', path='yolov5n.pt', source='local')
cap = cv2.VideoCapture(0)

base_url = 'https://api.telegram.org/bot??????????????????????????????/' # Bot token
send_message = 'sendMessage?chat_id={receiver_id}&text={message}'

contact = 000000000 # contact ID
text = 'Someone detected!'

while True:
    success, img = cap.read()
    result = model(img, size=640) # Reduce the size to increase the framerate
    table = result.pandas().xyxy[0]

    if 'person' in table.values:
        requests.get(base_url + send_message.format(receiver_id=contact, message=text))
        time.sleep(10)
