"""
Author: <Akinwunmi Eludoyin>
Assignment: #1
"""


# Step b: Create 4 variables

gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool


# Step c: Create a dictionary named workout_stats

# workout_stats is a dictionary where keys are strings and values are tuples of integers
workout_stats = {
    "Ola": (30, 45, 20),
    "Tunde": (25, 50, 30),
    "Sade": (40, 35, 25)
}


# Step d: Calculate total workout minutes using a loop and add to dictionary

for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes


# Step e: Create a 2D nested list called workout_list

# workout_list is a 2D list (list of lists) of integers
friend_names = [name for name in workout_stats.keys() if not name.endswith("_Total")]
workout_list = [list(workout_stats[name]) for name in friend_names]

print("Workout List:", workout_list)


# Step f: Slice the workout_list

# Yoga and Running for all friends
yoga_running = [row[0:2] for row in workout_list]
print("Yoga and Running (all friends):", yoga_running)

# Weightlifting for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting (last two friends):", weightlifting_last_two)


# Step g: Check if any friend's total >= 120

for friend in friend_names:
    total = workout_stats[f"{friend}_Total"]
    if total >= 120:
        print(f"Great job staying active, {friend}!")


# Step h: User input to look up a friend

search_name = input("Enter a friend's name: ")

if search_name in workout_stats and not search_name.endswith("_Total"):
    activities = workout_stats[search_name]
    total = workout_stats[f"{search_name}_Total"]
    print(f"{search_name}'s workout minutes:")
    print("Yoga:", activities[0])
    print("Running:", activities[1])
    print("Weightlifting:", activities[2])
    print("Total Minutes:", total)
else:
    print(f"Friend {search_name} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes

totals = {friend: workout_stats[f"{friend}_Total"] for friend in friend_names}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("Highest Total:", highest_friend, "-", totals[highest_friend])
print("Lowest Total:", lowest_friend, "-", totals[lowest_friend])
