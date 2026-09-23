import os
import datetime

# Check if diary.txt exists
if not os.path.exists("diary.txt"):
    try:
        # Create the file
        with open("diary.txt", "w") as file:
            pass
        print("diary.txt was created.")
    except Exception as e:
        print("Error creating diary.txt:", e)


# Get diary entry from the user
entry = input("Enter your diary entry: ")

# Get the current date and time
timestamp = datetime.datetime.now()

# Append the entry to the file
try:
    with open("diary.txt", "a") as file:
        file.write(f"{timestamp}: {entry}\n")

    print("\nDiary entry saved successfully!")

except Exception as e:
    print("Error writing to diary.txt:", e)


# Read and display the entire diary
try:
    with open("diary.txt", "r") as file:
        content = file.read()

    print("\n--- Your Diary ---")
    print(content)

except Exception as e:
    print("Error reading diary.txt:", e)