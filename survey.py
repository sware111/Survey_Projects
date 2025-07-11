import re

class Survey:
    def __init__(self, user):
        self.user = user

    def validate_recommend(self, rec):
        pattern = r'^\s*(yes|no)\s*$'
        return re.match(pattern, rec, re.IGNORECASE) is not None

    def run(self, conn):
        try:
            rate = int(input("From 1 to 5, how satisfied are you? "))
            if not 1 <= rate <= 5:
                print("Invalid number.")
                return
        except:
            print("Input must be a number..")
            return

        recommend = input("Do you recommend the course? (Yes/No): ")
        if not self.validate_recommend(recommend):
            print("Invalid answer")
            return

        opinion = input("Your opinion: ")

        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username=%s", (self.user.username,))
            user_id = cur.fetchone()[0]
            cur.execute("INSERT INTO responses (user_id, rate, recommend, opinion) VALUES (%s, %s, %s, %s)",
                        (user_id, rate, recommend.strip().lower() == 'yes', opinion))
        conn.commit()
        print("✅ Poll registered")