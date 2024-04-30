import Database
import login_gui

def main():
    login_gui.Login_System(Database.PayrollDatabase(), Database.UserDatabase())

if __name__ == "__main__":
    main()