import sqlite3 

# Connect to SQLite database (Creates file 'student.db' if not exists)
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Drop table if it already exists (to prevent errors when re-running)
cursor.execute("DROP TABLE IF EXISTS student")

# Create the table (Fixed VARCHAR issue)
table_info = """
CREATE TABLE student (
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INT
)
"""

cursor.execute(table_info)

# Insert records
cursor.execute("INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('John', 'Data Science', 'B', 100)")
cursor.execute("INSERT INTO STUDENT VALUES ('Mukesh', 'Data Science', 'A', 86)")
cursor.execute("INSERT INTO STUDENT VALUES ('Jacob', 'DevOps', 'A', 50)")
cursor.execute("INSERT INTO STUDENT VALUES ('Dipesh', 'DevOps', 'A', 35)")

# Display all records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Commit changes and close connection
connection.commit()
connection.close()
