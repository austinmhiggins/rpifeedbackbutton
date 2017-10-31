import sqlite3
import RPi.GPIO as GPIO
import time
import threading
from threading import Thread

conn = sqlite3.connect("feedback.db", check_same_thread=False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN,pull_up_down=GPIO.PUD_UP)

cursor = conn.cursor()

def positiveButton():
	while True:
		inputValue = GPIO.input(23)
		if (inputValue == False):

			cursor.execute("INSERT INTO feedback VALUES (001, date('now'), time('now'), 1)")
			conn.commit()
			print("Positive button press")
		time.sleep(.2)

def negativeButton():
	while True:
		inputValue = GPIO.input(25)
		if (inputValue == False):
			cursor.execute("INSERT INTO feedback VALUES (001, date('now'), time('now'), 2)")
			conn.commit()
			print("Negative button press")
		time.sleep(.2)

if __name__ == '__main__':
	Thread(target = positiveButton).start()
	Thread(target = negativeButton).start()

