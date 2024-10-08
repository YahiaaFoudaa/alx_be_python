# daily_reminder.py

def get_task():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def create_reminder(task, priority, time_bound):
    reminder = f"'{task}' is a {priority} priority task"
    
    match priority:
        case "high":
            reminder += " that requires immediate attention today!" if time_bound == "yes" else "Drop everything and work on it"
        case "medium":
            reminder += " that should be completed soon." if time_bound == "yes" else "completing it ASAP."
        case "low":
            reminder += " that can be done at your convenience." if time_bound == "yes" else "Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level entered."

    return reminder

def main():
    task, priority, time_bound = get_task()
    reminder = create_reminder(task, priority, time_bound)
    print(f"Reminder: '{reminder}")  # This is the print statement for the reminder

if __name__ == "__main__":
    main()
