import sqlite3
import time

# Ensure the database name is correct and in the correct folder 

conn = sqlite3.connect("feedback.db")
cursor = conn.cursor()

# Only prints contents of database to console

for row in cursor.execute("SELECT rowid, * FROM feedback ORDER BY device"):
	print row
