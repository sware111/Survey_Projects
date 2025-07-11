import psycopg2

class Database:

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="surveydb",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432"
        )

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def create_tables(self):
        cur = self.get_cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(20) UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            rate INTEGER CHECK (rate BETWEEN 1 AND 5),
            recommend BOOLEAN,
            opinion TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        self.commit()
        cur.close()