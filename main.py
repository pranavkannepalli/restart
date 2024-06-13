import RPi.GPIO as GPIO
from time import sleep
from pynput.keyboard import Controller, Key

keyboard = Controller()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

while True:
  if GPIO.input(2) == 0:
    print("Button pressed, restarting discord bot server")
    keyboard.press(Key.ctrl.value)
    keyboard.press('z')
    keyboard.release(Key.ctrl.value)
    keyboard.release('z')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(15)
    keyboard.type("cd ~/Documents/github/DiscordBot")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(5)
    keyboard.type("git pull")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(30)
    keyboard.type("pip install -r requirements.txt")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(60)
    keyboard.type("python main.py")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(30)
