from database import Database
from user import User
from survey import Survey
from utils import hash_password, log_activity
from analysis import generate_report

def main():
    db = Database()
    db.create_tables()
    conn = db.conn

    while True:
        print("\n1. Registration\n2. Login\n3. Reporting\n4. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            username = input("Username: ").strip()
            password = hash_password(input("Password: ").strip())
            user = User(username, password)
            user.save_to_db(conn)
            log_activity(username, "Registration")
            print("Registration completed.")
        elif choice == "2":
            username = input("Username: ").strip()
            password = hash_password(input("Password: ").strip())
            user = User.authenticate(conn, username, password)
            if user:
                log_activity(username, "Successful login")
                survey = Survey(user)
                survey.run(conn)
                log_activity(username, "Participate in the survey")
            else:
                print("The username or password is incorrect.")
        elif choice == "3":
            generate_report(conn)
        elif choice == "4":
            db.close()
            break
        else:
            print("The option is invalid.")

if __name__ == "__main__":
    main()