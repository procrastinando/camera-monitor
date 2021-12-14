import torch
import cv2
import time
from skpy import Skype
from getpass import getpass

model = torch.hub.load('', 'custom', path='yolov5n.pt', source='local')
cap = cv2.VideoCapture(0)

sk = Skype()
sk.conn.liveLogin("?????@????.com", getpass()) # Not Outlook mail
#sk.conn.soapLogin("?????@outlook.com", getpass()) # Outlook mail
contact = sk.contacts["live:?????"]
text = 'Someone detected!'

while True:
    success, img = cap.read()
    result = model(img, size=640) # Reduce the size to increase the framerate
    table = result.pandas().xyxy[0]

    if 'person' in table.values:
        contact.chat.sendMsg(text)
        time.sleep(10)
