from utils import hash_password

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self, conn):
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                        (self.username, self.password))
        conn.commit()

    @staticmethod
    def authenticate(conn, username, password):
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                        (username, password))
            user = cur.fetchone()
            if user:
                return User(username, password)
        return None