import pyttsx3
from plyer import notification
import time

def notify (title, message):
    notification.notify(title=title, message=message, timeout=6)

text = 'Hey Hacker, Complete the tasks today.'

engine = pyttsx3.init()

while True:
    notify ('Hey Hacker, Complete the tasks today.', message='Hey Hacker, Complete the tasks today.')
    engine.say(text)
    engine.runAndWait()
    time.sleep(1800)
