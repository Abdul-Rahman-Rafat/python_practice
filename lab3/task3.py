from datetime import datetime, date

def datetime_reminder():
    while True:
        user_input = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            reminder_date = datetime.strptime(user_input, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD (e.g., 2025-12-31).")

    today = date.today()
    delta = (reminder_date - today).days

    if delta < 0:
        print("This date has already passed.")
    else:
        with open("reminders.txt", "a") as file:
            file.write(f"{reminder_date} -> {delta} days left\n")
        print(f"Reminder saved: {reminder_date} -> {delta} days left")


