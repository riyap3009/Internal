#this program is gym workout helper
import datetime
import sys
#user details
login_keys= {}
with open("user.txt","r") as file:
    for line in file:
        line= line.strip()
        if ":" not in line:
            continue
        username,password,age= line.split(":")
        login_keys[username]=int(password)
def login():
    while True:
    
        entered_username=input("Enter your name: ")
        if entered_username not in login_keys:
            print("Invalid")
        else:
            break
            
    while True:
        entered_password=int(input("Enter your password: "))
        if entered_password == login_keys[entered_username]:
            print("Login Successful")
            return entered_username
        else:
            print("Please enter correct password")
    

def workout(current_user):
    while True:

        # Check body part
        while True:
            part = input("What part of the body are you focusing on today: ").lower()
            parts = ['legs', 'shoulders', 'arms', 'chest', 'back',
                     'glutes', 'core', 'triceps', 'forearms', 'abs', 'hamstring', 'cardio']
            if part in parts:
                break
            else:
                print("Enter a valid answer")

        workout = input("What workout/machine are you working on: ").lower()

        # Cardio workouts
        if workout in ["running", "walking", "sprints",
                       "treadmill", "cycling", "stairmaster,"]:

            unit = input("What unit is your distance (km/m): ")
            cardio = int(input(f"Distance running in {unit}: "))
            with open(f"workout.txt","a") as file:
                file.write(f"{username},{part},{workout},{cardio},{unit}\n")

        # Weight training workouts
        else:
            rep = int(input("How many reps are you achieving today?: "))
            breaks = int(input("Enter minutes of your break: "))
            with open("workout.txt","a") as file:
                file.write(f"{username},{part},{workout},{rep},{breaks}\n")

        question = input("Would you like to continue (yes/no): ").lower()

        if question == "no":
            x = datetime.datetime.now()
            print(x.year, x.strftime("%A %d %B %I:%M%p"))
            print("Have a good day")
            sys.exit()
        
           
current_user=login()
x=datetime.datetime.now()
print(x.year,x.strftime("%A %d %B %I:%M%p"))# prints the date and time automatically
workout(current_user)



