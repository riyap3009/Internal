#this program is gym workout helper
import datetime
import sys
password="Rover123"
AGE= 15
#user details
while True:
    
    name=input("Enter your name: ")
    if not name.isalpha(): #only accept letters
       print("Error please type name with letters only")
    else:
       break
while True:
    passwords=input("Enter your password: ")
    if passwords==password:
        break
    else:
        print("Please enter correct password")
while True:
    try:        
        age=int(input("Enter your age: "))
        if age<AGE:
            print('Your not eligible')
            sys.exit()
        break
        
    
    except ValueError:
            print("Enter numbers only")
    
x=datetime.datetime.now()
print(x.year,x.strftime("%A %d %B %I:%M%p"))# prints the date and time automatically

    
while True:
    while True:
        part=input("What part of the body are you focusing on today: ").lower()
        parts=['legs','shoulders','arms','chest','back','glutes','core','triceps','forearms','abs','hamstring']#defines different body parts that are worked on at the gym
        if part in parts:
            break
        else:
            print('Enter a valid answer')
    workout=input("What workout/machine are you working on: ").lower()
    
    if workout in ["running", "walking","sprints","treadmill","cycling","stairmaster"]:
        unit=input('What unit is your distance (km/m): ')
        cardio=int(input(f"Distance running in {unit}:  "))
        questions=input('Would you like to continue (yes/no): ')
        if questions == 'no':
            x=datetime.datetime.now()
            print(x.year,x.strftime("%A %d %B %I:%M%p"))
            print('Have a good day')
            sys.exit()
            
    else:
        rep=int(input("How many reps are your acheiving to do today?: "))
        breaks=int(input("Enter minutes of your break: "))
        question=input('Would you like to continue (yes/no): ')
        if question == 'no':
            x=datetime.datetime.now()
            print(x.year,x.strftime("%A %d %B %I:%M%p"))
            print("Have a good day")
            
            sys.exit()
            break
        




