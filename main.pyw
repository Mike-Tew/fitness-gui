# Todos
# Clean up body fat tab styling
# Bind return to all frames

from tkinter import (
    Tk,
    Frame,
    LabelFrame,
    Label,
    Entry,
    Button,
    Radiobutton,
    IntVar,
    END,
)
from tkinter import ttk

from formulas import (
    male_bmr,
    female_bmr,
    male_calories,
    female_calories,
    male_body_fat,
    bmi_formula,
)


def calculate_calories():
    """Get user inputs then calculate and display BMR and calorie data."""

    # Get all input data from the GUI
    age = float(age_input.get())
    weight = float(weight_input.get())
    height = float(height_input.get())
    heartrate = float(heartrate_input.get())
    duration = float(duration_input.get())

    if gender.get() == 0:
        # Calculate data for males
        bmr = male_bmr(weight, height, age)
        gross_calories = male_calories(heartrate, weight, age, duration)
    else:
        # Calculate data for females
        bmr = female_bmr(weight, height, age)
        gross_calories = female_calories(heartrate, weight, age, duration)

    net_calories = gross_calories - (bmr / 1440 * duration)

    # Display calculated data
    bmr_output.config(text=int(bmr))
    gross_output.config(text=int(gross_calories))
    net_output.config(text=int(net_calories))


def clear():
    # Clear input fields
    bmr_output.config(text="")
    gross_output.config(text="")
    net_output.config(text="")

    # Clear output text
    age_input.delete(0, END)
    weight_input.delete(0, END)
    height_input.delete(0, END)
    heartrate_input.delete(0, END)
    duration_input.delete(0, END)


def calculate_bmi():
    """Get user inputs and calculate their BMI"""

    # Get user inputs
    weight = float(bmi_weight_input.get())
    height = float(bmi_height_input.get())

    # Calculate and display BMI
    bmi_label.config(text=f"{bmi_formula(height, weight):.1f}")


root = Tk()
root.title("Exercise Calorie Calculator")
root.bind("<Return>", lambda x: calculate_calories())

# ---------------- TABS ---------------------
my_notebook = ttk.Notebook(root)
my_notebook.grid(row=0, column=0)

exercise_frame = Frame(my_notebook)
body_fat_frame = Frame(my_notebook)
bmi_frame = Frame(my_notebook)

my_notebook.add(exercise_frame, text="Exercise Calc")
my_notebook.add(body_fat_frame, text="Body Fat Calc")
my_notebook.add(bmi_frame, text="BMI Calc")

# ---------------- EXERCISE TAB -------------------
exercise_title = Label(
    exercise_frame,
    text="EXERCISE CALORIE CALCULATOR",
    pady=10,
    font=("Helvetica 12 bold"),
)
exercise_title.grid(row=0, column=0, columnspan=2)
gender = IntVar()
input_frame = LabelFrame(exercise_frame, text="Input", padx=20, pady=10)
input_frame.grid(row=1, column=0, padx=10)

# Exercise data inputs and labels
age_label = Label(input_frame, text="Age")
age_label.grid(row=0, column=0, columnspan=2)
age_input = Entry(input_frame, width=10)
age_input.grid(row=1, column=0, columnspan=2)

weight_label = Label(input_frame, text="Weight (lb)")
weight_label.grid(row=2, column=0, pady=[10, 0], columnspan=2)
weight_input = Entry(input_frame, width=10)
weight_input.grid(row=3, column=0, columnspan=2)

height_label = Label(input_frame, text="Height (in)")
height_label.grid(row=4, column=0, pady=[10, 0], columnspan=2)
height_input = Entry(input_frame, width=10)
height_input.grid(row=5, column=0, columnspan=2)

duration_label = Label(input_frame, text="Minutes")
duration_label.grid(row=6, column=0, pady=[10, 0], columnspan=2)
duration_input = Entry(input_frame, width=10)
duration_input.grid(row=7, column=0, columnspan=2)

heartrate_label = Label(input_frame, text="Heartrate")
heartrate_label.grid(row=8, column=0, pady=[10, 0], columnspan=2)
heartrate_input = Entry(input_frame, width=10)
heartrate_input.grid(row=9, column=0, columnspan=2)

# Gender radio buttons
r1 = Radiobutton(input_frame, text="Male", variable=gender, value=0)
r1.grid(row=10, column=0, pady=[10, 0])

r2 = Radiobutton(input_frame, text="Female", variable=gender, value=1)
r2.grid(row=10, column=1, pady=[10, 0])

output_frame = LabelFrame(exercise_frame, text="Output")
output_frame.grid(row=1, column=1, ipady=21, padx=10)

# Labels for text output
bmr_label = Label(output_frame, text="BMR", font="bold")
bmr_label.grid(row=1, column=0, padx=30, pady=[30, 0])
bmr_output = Label(output_frame, font=("Helvetica 15 bold"))
bmr_output.grid(row=2, column=0)

gross_label = Label(output_frame, text="Gross Calories", font="bold", padx=25)
gross_label.grid(row=4, column=0, pady=[30, 0])
gross_output = Label(output_frame, font=("Helvetica 15 bold"))
gross_output.grid(row=5, column=0)

net_label = Label(output_frame, text="Net Calories", font="bold")
net_label.grid(row=7, column=0, pady=[31, 0])
net_output = Label(output_frame, font=("Helvetica 15 bold"))
net_output.grid(row=8, column=0)

# Create the calculate button
calculate_button = Button(
    exercise_frame, width=15, text="Calculate", command=calculate_calories
)
calculate_button.grid(row=2, column=0, pady=[20, 0], padx=20)

# Create the clear button
clear_button = Button(exercise_frame, width=15, text="Clear", command=clear)
clear_button.grid(row=2, column=1, pady=[20, 0])

# Create the exit button
exit_button = Button(exercise_frame, width=20, text="Exit", command=root.quit)
exit_button.grid(row=3, column=0, pady=[20, 10], columnspan=2)

# -------------------------- BODY FAT TAB -----------------------
body_fat_label = Label(
    body_fat_frame, text="BODY FAT CALCULATOR", pady=10, font=("Helvetica 12 bold")
)
body_fat_label.grid(row=0, column=0, columnspan=2)

body_fat_input_frame = LabelFrame(body_fat_frame, text="Input", padx=20, pady=10)
body_fat_input_frame.grid(row=1, column=0, padx=10)

# Body Fat Labels And Inputs
bf_age_label = Label(body_fat_input_frame, text="Age")
bf_age_label.grid(row=1, column=0)
bf_age_input = Entry(body_fat_input_frame, width=15)
bf_age_input.grid(row=2, column=0, pady=[0, 10])

bf_weight_label = Label(body_fat_input_frame, text="Weight")
bf_weight_label.grid(row=3, column=0)
bf_weight_input = Entry(body_fat_input_frame, width=15)
bf_weight_input.grid(row=4, column=0, pady=[0, 10])

bf_chest_label = Label(body_fat_input_frame, text="Chest Skinfold")
bf_chest_label.grid(row=5, column=0)
bf_chest_input = Entry(body_fat_input_frame, width=15)
bf_chest_input.grid(row=6, column=0, pady=[0, 10])

bf_ab_label = Label(body_fat_input_frame, text="Ab Skinfold")
bf_ab_label.grid(row=7, column=0)
bf_ab_input = Entry(body_fat_input_frame, width=15)
bf_ab_input.grid(row=8, column=0, pady=[0, 10])

bf_thigh_label = Label(body_fat_input_frame, text="Thigh Skinfold")
bf_thigh_label.grid(row=9, column=0)
bf_thigh_input = Entry(body_fat_input_frame, width=15)
bf_thigh_input.grid(row=10, column=0, pady=[0, 10])

# Body Fat Output Area
body_fat_output_frame = LabelFrame(body_fat_frame, text="Output", padx=20, pady=10)
body_fat_output_frame.grid(row=1, column=1)

bf_label = Label(body_fat_output_frame, text="Body Fat", font="bold")
bf_label.grid(row=1, column=0, padx=30, pady=[30, 0])
bf_output = Label(body_fat_output_frame, font=("Helvetica 15 bold"))
bf_output.grid(row=2, column=0)

fat_mass_label = Label(body_fat_output_frame, text="Fat Mass", font="bold")
fat_mass_label.grid(row=4, column=0, pady=[30, 0])
fat_mass_output = Label(body_fat_output_frame, font=("Helvetica 15 bold"))
fat_mass_output.grid(row=5, column=0)

lean_mass_label = Label(body_fat_output_frame, text="Lean Mass", font="bold")
lean_mass_label.grid(row=7, column=0, pady=[31, 0])
lean_mass_output = Label(body_fat_output_frame, font=("Helvetica 15 bold"))
lean_mass_output.grid(row=8, column=0)


def calculate_body_fat():
    age = float(bf_age_input.get())
    weight = float(bf_weight_input.get())
    chest = float(bf_chest_input.get())
    ab = float(bf_ab_input.get())
    thigh = float(bf_thigh_input.get())

    body_fat = male_body_fat(age, chest, ab, thigh)
    fat_mass = weight * body_fat * 0.01

    bf_output.config(text=f"{body_fat:.1f}%")
    fat_mass_output.config(text=f"{fat_mass:.1f} lb")
    lean_mass_output.config(text=f"{weight - fat_mass:.1f} lb")


# Create the calculate button
calculate_button = Button(
    body_fat_frame, width=15, text="Calculate", command=calculate_body_fat
)
calculate_button.grid(row=2, column=0, pady=[20, 0], padx=20)

# Create the clear button
clear_button = Button(body_fat_frame, width=15, text="Clear", command=clear)
clear_button.grid(row=2, column=1, pady=[20, 0])

# Create the exit button
exit_button = Button(body_fat_frame, width=20, text="Exit", command=root.quit)
exit_button.grid(row=3, column=0, pady=[20, 10], columnspan=2)


# ----------------------------- BMI TAB ------------------------
bmi_label = Label(
    bmi_frame, text="BODY MASS INDEX", pady=10, font=("Helvetica 12 bold")
)
bmi_label.grid(row=0, column=0, columnspan=2)

bmi_input_frame = LabelFrame(bmi_frame, text="Input", padx=20, pady=10)
bmi_input_frame.grid(row=1, column=0, padx=10)

# BMI Weight Label And Input
bmi_weight_label = Label(bmi_input_frame, text="Weight")
bmi_weight_label.grid(row=1, column=0)
bmi_weight_input = Entry(bmi_input_frame, width=15)
bmi_weight_input.grid(row=2, column=0, pady=[0, 10])
bmi_pound_label = Label(bmi_input_frame, text="lb")
bmi_pound_label.grid(row=2, column=1)

# BMI Height Labels And Inputs
bmi_height_label = Label(bmi_input_frame, text="Height (in inches)")
bmi_height_label.grid(row=3, column=0)
bmi_height_input = Entry(bmi_input_frame, width=15)
bmi_height_input.grid(row=4, column=0)
bmi_inch_label = Label(bmi_input_frame, text="in")
bmi_inch_label.grid(row=4, column=1)

bmi_output_frame = LabelFrame(bmi_frame, text="Output", padx=20, pady=10)
bmi_output_frame.grid(row=1, column=1, padx=10)

# BMI output labels
bmi_output_label = Label(bmi_output_frame, text="BMI", font="bold", padx=45)
bmi_output_label.grid(row=0, column=0, pady=[23, 0])

bmi_label = Label(bmi_output_frame, text="--.-", font=("Helvetica 15 bold"))
bmi_label.grid(row=1, column=0, pady=7)

# Create the calculate button
calculate_button = Button(bmi_frame, width=20, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, column=0, pady=[20, 0], padx=20, columnspan=2)

# Create the exit button
exit_button = Button(bmi_frame, width=20, text="Exit", command=root.quit)
exit_button.grid(row=3, column=0, pady=[20, 10], columnspan=2)

root.mainloop()
