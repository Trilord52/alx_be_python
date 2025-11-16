task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
while priority not in ["high", "medium", "low"]:
    priority = input("Invalid input! Enter high, medium, or low: ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
while time_bound not in ["yes", "no"]:
    time_bound = input("Invalid input! Enter yes or no: ").lower()
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
print(f"Reminder: {reminder}")
