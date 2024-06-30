# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
if priority == 'high':
    reminder = f" '{task}' is a high priority task"
elif priority == 'medium':
    reminder = f" '{task}' is a medium priority task"
elif priority == 'low':
    reminder = f" '{task}' is a low priority task"
else:
    reminder = f" '{task}' has an unknown priority level"

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"


# Print the customized reminder
print("Reminder:", reminder)

# Additional note for non-time-bound tasks
if time_bound == 'no':
    print(f"Note: '{task}' is a {priority} priority task. Consider completeing it when you have free time.")
