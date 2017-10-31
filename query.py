import sqlite3
import time

conn = sqlite3.connect("feedback.db")
cursor = conn.cursor()

for row in cursor.execute("SELECT rowid, * FROM feedback ORDER BY device"):
	print row