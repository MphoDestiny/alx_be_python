# daily_reminder.py

# Prompt user for daily details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case 'high':
        reminder = f" '{task}' is a high priority task"
    case 'medium':
        reminder = f" '{task}' is a medium priority task"
    case 'low':
        reminder = f" '{task}' is a low priority task"
    case_:
        reminder = f" '{task}' has an unknown priority level"

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print("Reminder:", reminder)

# Additional note for non-time-bound tasks
if time_bound == 'no':
    print(f"Note: '{task}' is a {priority} priority task. Consider completeing it when you have free time.")
