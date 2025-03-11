import sqlite3
import time

class SQLiteConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.start_time = time.time()
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = (self.end_time - self.start_time)
        if self.connection:
            self.connection.close()
        return False

def create_users_table(db_name):
    with SQLiteConnection(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

if __name__ == "__main__":
    db_name = 'example.db'
    create_users_table(db_name)
    print("Users table created (if it did not exist).")
