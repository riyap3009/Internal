#This program ilkm the final version of Workout Helper for gym people. This program uses tkinter 
from tkinter import *
import datetime
import matplotlib.pyplot as plt
from tkinter import messagebox
#----------------------Functions----------------------
def show_frame(frame):
    frame.tkraise()
#-------------------------SignUp---------------------------------
def signup():
    username = signup_username_Entry.get()
    password = signup_password_Entry.get()
    age = signup_age_Entry.get()

    if username == "" or password == "" or age == "":
        messagebox.showinfo("Error", "Please fill in all fields")
        return

    try:
        password = int(password)
        age = int(age)
    except ValueError:
        messagebox.showinfo("Error", "Password and age must be numbers")
        return

    if age < 15:
        messagebox.showinfo("Error", "You must be at least 15 years old")
        return

    if username in login_keys:
        messagebox.showinfo("Error", "Username already exists")
        return

    with open("user.txt", "a") as file: #"a" indicates to add new data to that external file
        file.write(f"{username}:{password}:{age}\n")

    login_keys[username] = { #[username] is used to find the the username int he external file
        "password": password,
        "age": age
    }

    messagebox.showinfo("Success", "Account Created")
    show_frame(login_frame)

#--------------------------Login--------------------------------------
def login():
    global current_user

    username = username_Entry.get()
    password = password_Entry.get()

    if username not in login_keys:
        messagebox.showinfo("Error", "Username not found")
        return

    try:
        password = int(password)
    except ValueError:
        messagebox.showinfo("Error", "Password must be a number")
        return

    if login_keys[username]["password"] == password:
        current_user = username
        messagebox.showinfo("Success", "Login Successful")
        show_frame(workout_frame)
        x= datetime.datetime.now()
        messagebox.showinfo(x.year, x.strftime("%A %d %B %I:%M%p"))
    else:
        messagebox.showinfo("Error", "Incorrect Password")


#-----------------------------Logging Out-------------------------------------
def logout():
    global current_user
    current_user = None
    show_frame(home_frame)
    x= datetime.datetime.now()
    messagebox.showinfo(x.year, x.strftime("%A %d %B %I:%M%p"))
#-------------------------Saving the data-----------------------------------------
def save():
    workout = workout_Entry.get()
    value = value_Entry.get().strip()
    part = body_part.get()

    if workout == "" or value == "":
        messagebox.showinfo("Error", "Enter workout details")
        return
    try:
        value=int(value)
    except ValueError:
        messagebox.showinfo("Error, only numbers allowed e.g:10")

    x= datetime.datetime.now()
    messagebox.showinfo(x.year, x.strftime("%A %d %B %I:%M%p"))

    with open("workout.txt", "a") as file:
        file.write(
            f"{current_user}:{x.date()}:{part}:{workout}:{value}\n"
        )

    messagebox.showinfo("Success", "Workout Saved")

#------------------------------Uploading Graph------------------------------------------------
def graph():
    data = {}

    try:
        with open("workout.txt", "r") as file:#"r" indciates that the program reads the data from the external file and displays it for the user to see
            for line in file:
                username, date, part, workout, value = line.strip().split(":")#line.split(:) indicates the data can is seperated by colons.

                if username == current_user:
                    data[part] = data.get(part, 0) + int(value)# adds up the total reps or distance with the particular part of the body. Start at 0 indicating no value 

    except ValueError:
        messagebox.showinfo("Error", "No workout data found")
        return

    if data == {}:
        messagebox.showinfo("Error", "No workouts saved")
        return

    plt.bar(list(data.keys()), list(data.values()))
    plt.xlabel("Body Part")
    plt.ylabel("Total Reps")
    plt.title(f"{current_user}'s Workout Summary")
    plt.show()


#----------------------Load Users into Program----------------------
current_user = None
login_keys = {}

try:
    with open("user.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            username, password, age = line.split(":")

            login_keys[username] = {
                "password": int(password),
                "age": int(age)
            }

except ValueError:
    pass# no code so no error continue


#----------------------Main Window----------------------
root = Tk()
root.title("Gym Workout Helper")
root.geometry("600x600")
home_photo=PhotoImage(file="gyms.png")
home_photo=home_photo.subsample(4,4)

# ---------------------- Frames ----------------------
home_frame = Frame(root,)
login_frame = Frame(root)
signup_frame = Frame(root)
workout_frame = Frame(root)

for frame in (home_frame, login_frame, signup_frame, workout_frame):
    frame.grid(row=0, column=0, sticky="nsew")
#----------------------Home Page----------------------
Label(
    home_frame,
    image=home_photo).grid(row=0, column=0, pady=10)

Label(
    home_frame,
    text="Gym Workout Helper",
    font=("Arial", 16, "bold underline")
).grid(row=0, column=2,)

Button(
    home_frame,
    text="Login",
    command=lambda: show_frame(login_frame,)
).grid(row=1, column=2, padx=10, pady=20)

Button(
    home_frame,
    text="Sign Up",
    command=lambda: show_frame(signup_frame)
).grid(row=2, column=2, padx=10, pady=20)

Label(
    home_frame,
    text="This program was created by @Riya Patel for educational purposes.\n"
    "All rights reserved.",
    font=("Arial",14,"underline")
).grid(row=3, column=2)
    
                

#----------------------Login Page----------------------
Label(
    login_frame,
    text="Login",
    font=("Arial", 16, "bold underline")
).grid(row=0, column=3,pady=20)

Label(login_frame, text="Username:").grid(row=1, column=2)
username_Entry = Entry(login_frame)
username_Entry.grid(row=1, column=3)
username_Entry.focus_set()


Label(login_frame, text="Password:").grid(row=2, column=2)
password_Entry = Entry(login_frame, show="*")
password_Entry.grid(row=2, column=3)

Button(
    login_frame,
    text="Login",
    bg="white",
    fg="black",
    relief="groove",
    command=login
).grid(row=3, column=3,pady=10)

Button(
    login_frame,
    text="Back",
    bg="white",
    fg="black",
    relief="groove",
    command=lambda: show_frame(home_frame)
).grid(row=4, column=3,pady=10)

login_photo=PhotoImage(file="dumbells.png")
login_photo=login_photo.subsample(5,5)

Label(
    login_frame,
    image=login_photo
).grid(row=5, column=3,)



#----------------------Sign Up Page----------------------
Label(
    signup_frame,
    text="Sign Up",
    font=("Arial", 16, "bold underline")
).grid(row=0, column=1, columnspan=2, pady=20)

Label(signup_frame, text="Username").grid(row=1, column=0)
signup_username_Entry = Entry(signup_frame)
signup_username_Entry.grid(row=1, column=1)
signup_username_Entry.focus_set()

Label(signup_frame, text="Password").grid(row=2, column=0)
signup_password_Entry = Entry(signup_frame)
signup_password_Entry.grid(row=2, column=1)

Label(signup_frame, text="Age").grid(row=3, column=0)
signup_age_Entry = Entry(signup_frame)
signup_age_Entry.grid(row=3, column=1)

Button(
    signup_frame,
    text="Create Account",
    command=signup
).grid(row=4, column=1,  pady=10)

Button(
    signup_frame,
    text="Back",
    command=lambda:show_frame(home_frame,)
).grid(row=4, column=3,)

signup_photo=PhotoImage(file="dumbells.png")
signup_photo=signup_photo.subsample(5,5)

Label(
    signup_frame,
    image=signup_photo
).grid(row=6, column=4,)

#----------------------Workout Page----------------------

Label(
    workout_frame,
    text="Workout Helper",
    font=("Arial", 16,"bold underline")
).grid(row=0, column=0, pady=20)

Label(
    workout_frame,
    text="What part of the body are you focusing on today: ",
    font=("Arial", 16,)
).grid(row=1, column=0, pady=20,padx=20)

Label(
    workout_frame,
    text="Click on the following button",
    font=("Italic", 14,)
).grid(row=2,column=0,)


body_part = StringVar()
body_part.set("legs")

parts = [
    "legs", "arms", "chest", "back",
    "shoulders", "core", "cardio"
]

row_num = 3# starts at row 3 because row 3 is taken
for part in parts:
    Radiobutton(
        workout_frame,
        text=part.capitalize(),#first letter is uppercase
        variable=body_part,
        value=part
    ).grid(row=row_num, column=0, sticky="w",pady=5, padx=10)
    row_num += 3 #start at row 2 and continues however many rows in the list parts

Label(workout_frame, text="Workout Name").grid(row=row_num, column=0)
workout_Entry = Entry(workout_frame,bg="white",fg="black")
workout_Entry.grid(row=row_num+1, column=0)
row_num += 3

Label(workout_frame, text="Reps/Distance").grid(row=row_num, column=0)
value_Entry = Entry(workout_frame,bg="white",fg="black")
value_Entry.grid(row=row_num+1, column=0)
row_num += 3

Button(
    workout_frame,
    text="Save Workout",   
    command=save
).grid(row=row_num, column=0, columnspan=2, pady=5)
row_num += 3

Button(
    workout_frame,
    text="Show Progress Graph",
    command=graph
).grid(row=row_num, column=0, columnspan=2, pady=5)
row_num += 3

Button(
    workout_frame,
    text="Logout",
    command=logout
).grid(row=row_num, column=0, columnspan=2, pady=5)

#----------------------Start Program----------------------
show_frame(home_frame)
root.mainloop()
