import sqlite3
from pathlib import Path

ABSOLUTE_APPLICATION_PATH = Path(__file__).resolve().parents[0]
DB_PATH = ABSOLUTE_APPLICATION_PATH / 'todo.db'

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS todo")
    
    cursor.execute("""
        CREATE TABLE todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            task CHAR(100) NOT NULL, 
            status BOOLEAN NOT NULL
        )
    """)
    
    cursor.execute("INSERT INTO todo (task, status) VALUES ('Read the Python tutorial to get a good introduction into Python', 1)")
    cursor.execute("INSERT INTO todo (task, status) VALUES ('Visit the Python website', 1)")
    cursor.execute("INSERT INTO todo (task, status) VALUES ('Test various editors for and check the syntax highlighting', 1)")
    cursor.execute("INSERT INTO todo (task, status) VALUES ('Choose your favorite WSGI-Framework', 0)")
    
    connection.commit()

print("Database 'todo.db' initialized successfully.")