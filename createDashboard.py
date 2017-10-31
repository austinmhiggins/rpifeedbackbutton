import sqlite3
import time

conn = sqlite3.connect("feedback.db")

cursor = conn.cursor()

cursor.execute ( """ CREATE TABLE feedback
		(device integer, date date, time time,
		action integer)
		""")

conn.commit()