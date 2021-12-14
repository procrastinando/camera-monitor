# camera-monitor
This shows a method to monitor a camera through skype or telegram using python and yolov5

## Requirements
```bash
python3
pytorch
opencv
skpy
telepot
```

## Setup
```bash
git clone https://github.com/procrastinando/camera-monitor
pip -r install requirements.txt
```

## Skype setup
1. Create a Skype account and login though the browser: https://web.skype.com/
2. Use the credential to login running run_skype.py
```python run_skype.py```

## Telegram setup
1. Create a bot using BotFather
2. Save the token and get the receiver ID (https://apt.telegram.org/bot <TOKEN> /getUpdates)
3. Use the token and the receiver ID to edit run_telegram.py
```python run_telegram.py```
