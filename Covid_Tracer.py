#Name: MENDIOLA, LOGIE | Year & Section: BSCPE 1-5 | Object Oriented Programming | Finals Project

#Instructions:
#Create “your” own covid contact tracing app with GUI
#Create a program that ask user for typical information found in covid contact tracing app
#Write the collected information in a file (use any format you like)
#The app should be able to add and search entry
#Please don’t follow any online contact tracing programming tutorial


####### LAYOUT DRAFT FOR PROGRAM ######

#Main Window
from tkinter import *
import tkinter as tk

from tkinter import messagebox

#Call another file to overwrite and save data entry
def covid_prompt_info(info):
    with open("covid_contact_entry.txt", "a") as entry_file:
        for key, value in info.items():
            entry_file.write(f"{key}: {value}\n")
        entry_file.write(str(info) + "\n")

#Record of input entries from users
def submit_records():
    symptom_four_values = {
        "Fever": symptom_four_chk1_var.get(),
        "Cough": symptom_four_chk2_var.get(),
        "Colds": symptom_four_chk3_var.get(),
        "Muscle/body pains": symptom_four_chk4_var.get(),
        "Sore Throat": symptom_four_chk5_var.get(),
        "Diarrhea": symptom_four_chk6_var.get(),
        "None of the above": symptom_four_chk7_var.get(),
        "Headache": symptom_four_chk8_var.get(),
        "Shortness of breath": symptom_four_chk9_var.get(),
        "Difficulty of breathing": symptom_four_chk10_var.get(),
        "Loss of taste": symptom_four_chk11_var.get(),
        "Loss of smell": symptom_four_chk12_var.get()
    }

    data = {
        "First Name": first_name_prsnl_input.get(),
        "Middle Name": middle_name_prsnl_input.get(),
        "Last Name": last_name_prsnl_input.get(),
        "Current Address": current_address_prsnl_input.get("1.0", "end-1c"),
        "Permanent Address": permanent_address_prsnl_input.get("1.0", "end-1c"),
        "Birth Date": calendar.get_date(),
        "Contact Number / Landline": contact_prsnl_input.get(),
        "E-mail Address": email_prsnl_input.get(),
        "Occupation": occupy_prsnl_input.get(),
        "Workplace Name / School Name": workplace_name_input.get(),
        "Workplace Address / School Address": workplace_add_input.get(),
        "Emergency Contact - Name": name_emrgncy_input.get(),
        "Emergency Contact - Address": address_emergncy_input.get(),
        "Emergency Contact - Contact Number / Landline": contact_emergncy_input.get(),
        "Emergency Contact - E-mail Address": email_emergncy_input.get(),
        "Emergency Contact - Relationship": relationship_emergncy_input.get(),
        "Have you been vaccinated for COVID-19?": symptom_one.get(),
        "What is your current dose/booster of vaccination shot?": symptom_two.get(),
        "What is the brand of your vaccination for COVID-19?": covid_symptom_three_input.get(),
        "Are you experiencing symptoms in the past 7 days?": symptom_four_values,   
        "Have you had exposure to probable or confirm case in the last 7 days?": symptom_five.get(),
        "Have you had contact with others with COVID-19 Symptoms in the last 7 days?": symptom_six.get(),
        "Have you been tested for COVID-19 in the last 14 days?": symptom_seven.get(),
        "Most recent visited area/place?": addtnl_one_input.get(),
        "Number of people you saw in the visited area/place?": addtnl_two_input.get(),
        "Mode of Transportation": additional_three_qstn.get(),
        "Recent Medication Intake / Vitamin Intake?": addtnl_four_input.get()
    }
    covid_prompt_info(data)

    # Should ask user to confirm if the inputs are correct or not (Yes or No, Continue Editing)
    # If Yes, End Program
    # If Not, should be able to edit given data again
    response = messagebox.askyesno("Data Collection Complete!", "Do you want to save the data?")

    if response:
        covid_prompt.destroy()

#function for searching entries
def scan_covid_prompt_info():
    #use for searching for keywords in the search entry
    keywords = identify_search.get().lower()
    print("Searching for:", keywords)

    matching_entry = []
    entry_record = {}
    with open("covid_contact_entry.txt", "r") as entry_file:
        entry_lines = entry_file.readlines()
        for line in entry_lines:
            if not line.strip():
                
                if entry_record:

                    # Check if the keyword exists in any of the values of the entry
                    if any(keywords in val.lower() for val in entry_record.values()):
                        matching_entry.append(entry_record.copy())
                    entry_record = {}
            else:
                if ':' in line:
                    key, value = line.strip().split(': ', 1)
                    entry_record[key] = value

    # Check the last entry if there was no blank line after it
    if entry_record:
        if any(keywords in val.lower() for val in entry_record.values()):
            matching_entry.append(entry_record)

    # Display the results from the search entry
    if matching_entry:
        entry_result = []
        for entry in matching_entry:
            entry_value = "\n".join([f"{key}: {value}" for key, value in entry.items()])
            entry_result.append(entry_value)
        results = "\n\n".join(entry_result)
        print(results)

    else:
        print("No matching results found.")

covid_prompt = tk.Tk()
covid_prompt.title("(CCT) Covid Contact Tracer - BetaTest v.0.0")
covid_prompt.geometry("1530x1530")

#Entry widget for the main window
covid_contact_entry = tk.Entry(covid_prompt)


#Pre-Form Message
pre_form_message = Label(covid_prompt, text ="Fill out the form with outmost honesty for safety measures and the well being of others.\nMaraming Salamat Po!")
pre_form_message.place(x = 10, y = 20)


#Form for Asking Personal Questions:
# Name: (First Name, Middle Name, Last Name)
first_name_prsnl = Label(covid_prompt, text = "First Name:")
first_name_prsnl.place(x = 10, y = 60)

first_name_prsnl_input = Entry(covid_prompt, width = "30")
first_name_prsnl_input.place(x = 10, y = 80)

middle_name_prsnl = Label(covid_prompt, text = "Middle Name:")
middle_name_prsnl.place(x = 220, y = 60)

middle_name_prsnl_input = Entry(covid_prompt, width = "30")
middle_name_prsnl_input.place(x = 220, y = 80)

last_name_prsnl = Label(covid_prompt, text = "Last Name:")
last_name_prsnl.place(x = 10, y = 110)

last_name_prsnl_input = Entry(covid_prompt, width = "30")
last_name_prsnl_input.place(x = 10, y = 130)

# - Address: (Current & Permanent)
current_address_prsnl = Label(covid_prompt, text = "Current Address:")
current_address_prsnl.place(x = 10, y = 180)

current_address_prsnl_input = Text(covid_prompt, width = "23", height = "10")
current_address_prsnl_input.place(x = 10, y = 200)

permanent_address_prsnl = Label(covid_prompt, text = "Permanent Address:")
permanent_address_prsnl.place(x = 220, y = 180)

permanent_address_prsnl_input = Text(covid_prompt, width = "23", height = "10")
permanent_address_prsnl_input.place(x = 220, y = 200)

# - Birthdate:
birth_date = Label(covid_prompt, text ="Birth Date:")
birth_date.place(x = 10, y = 400)

from tkcalendar import Calendar
calendar = Calendar(covid_prompt, selectmode = 'day', year = 2023, month = 7, day = 18)
calendar.place(x = 10, y = 430)

# - Contact Number/Landline:
contact_prsnl = Label(covid_prompt, text = "Contact Number / Landline:")
contact_prsnl.place(x = 10, y = 630)

contact_prsnl_input = Entry(covid_prompt, width = "30")
contact_prsnl_input.place(x = 10, y = 650)

# - Email Address:
email_prsnl = Label(covid_prompt, text = "E-mail Address:")
email_prsnl.place(x = 10, y = 680)

email_prsnl_input = Entry(covid_prompt, width = "30")
email_prsnl_input.place(x = 10, y = 700)

# - Occupation:
occupy_prsnl = Label(covid_prompt, text = "Occupation:")
occupy_prsnl.place(x = 10, y = 730)

occupy_prsnl_input = Entry(covid_prompt, width = "30")
occupy_prsnl_input.place(x = 10, y = 750)

# - Workplace Name/ School or University Name:
workplace_name = Label(covid_prompt, text = "Workplace Name / School Name:")
workplace_name.place(x = 220, y = 630)

workplace_name_input = Entry(covid_prompt, width= "30")
workplace_name_input.place(x = 220, y = 650)

# - Workplace Address / School or University Address
workplace_add = Label(covid_prompt, text = "Workplace Address / School Address:")
workplace_add.place(x = 220, y= 680)

workplace_add_input = Entry(covid_prompt, width = "30")
workplace_add_input.place (x = 220, y = 700)

#Emergency Contact:
emergency_contact = Label(covid_prompt, text = "Emergency Contact")
emergency_contact.place(x = 600, y = 10)


# -Name (First Name, Last Name)
name_emrgncy = Label(covid_prompt, text = "Name (First Name, Last Name):")
name_emrgncy.place(x = 600, y = 30)

name_emrgncy_input = Entry(covid_prompt, width ="30")
name_emrgncy_input.place(x = 600, y = 50)

# -Address:
address_emergncy = Label(covid_prompt, text = "Address:")
address_emergncy.place(x = 820, y= 30)

address_emergncy_input = Entry(covid_prompt, width ="30")
address_emergncy_input.place(x = 820, y = 50)

# -Contact Number/Landline
contact_emergncy = Label(covid_prompt, text = "Contact Number / Landline:")
contact_emergncy.place(x = 600, y = 90)

contact_emergncy_input = Entry(covid_prompt, width = "30")
contact_emergncy_input.place(x = 600, y = 110)

# -Email Address
email_emergncy = Label(covid_prompt, text ="E-mail Address:")
email_emergncy.place(x = 820, y = 90)

email_emergncy_input = Entry(covid_prompt, width ="30")
email_emergncy_input.place(x = 820, y = 110)

# -Relationship to the Contact Person
relationship_emergncy = Label(covid_prompt, text = "Relationship to the Contact Person:")
relationship_emergncy.place(x = 600, y = 150)

relationship_emergncy_input = Entry(covid_prompt, width="30")
relationship_emergncy_input.place(x =600, y = 180)


#Questions to Assure Covid Symptoms of User:
covid_symptom = Label(covid_prompt, text = "Assessment for Signs and Symptoms of Covid-19")
covid_symptom.place(x = 600, y = 200)

# - Have you been vaccinated for COVID-19?
covid_symptom_one = Label(covid_prompt, text = "Have you been vaccinated for COVID-19?")
covid_symptom_one.place(x = 600, y = 240)

symptom_one = IntVar()
covid_symptom_one_rbtn1 = Radiobutton(covid_prompt, text = "Yes", variable = symptom_one, value = "1")
covid_symptom_one_rbtn1.place(x = 600, y = 260)

covid_symptom_one_rbtn2 = Radiobutton(covid_prompt, text = "No", variable = symptom_one, value = "2")
covid_symptom_one_rbtn2.place(x = 600, y = 280)

# What is your current number of vaccination shot?
covid_symptom_two = Label(covid_prompt, text = "What is your current dose/booster of vaccination shot?")
covid_symptom_two.place(x = 600, y = 320)

symptom_two = IntVar()
covid_symptom_two_rbtn1 = Radiobutton(covid_prompt, text = "1st Dose", variable = symptom_two, value = "1")
covid_symptom_two_rbtn1.place(x = 600, y = 340)

covid_symptom_two_rbtn2 = Radiobutton(covid_prompt, text = "2nd Dose", variable = symptom_two, value = "2")
covid_symptom_two_rbtn2.place(x = 600, y = 360)

covid_symptom_two_rbtn3 = Radiobutton(covid_prompt, text = "1st Booster", variable = symptom_two, value = "3")
covid_symptom_two_rbtn3.place(x = 600, y = 380)

covid_symptom_two_rbtn4 = Radiobutton(covid_prompt, text = "2nd Booster", variable = symptom_two, value = "4")
covid_symptom_two_rbtn4.place(x = 600, y = 400)

covid_symptom_two_rbtn5 = Radiobutton(covid_prompt, text = "N/A", variable = symptom_two, value = "5")
covid_symptom_two_rbtn5.place(x = 600, y = 420)


# - What is the brand of your COVID-19 Vaccination
covid_symptom_three = Label(covid_prompt, text = "What is the brand of your vaccination for COVID-19?")
covid_symptom_three.place(x = 600, y = 460)

covid_symptom_three_input = Entry(covid_prompt, width = "30")
covid_symptom_three_input.place(x = 600, y = 480)

# - Are you experiencing symptoms in the past 7 days
covid_symptom_four = Label(covid_prompt, text = "Are you experiencing these symptoms in the past 7 days?")
covid_symptom_four.place(x = 600, y = 510)

symptom_four_chk1_var = IntVar()
symptom_four_chk1 = Checkbutton(covid_prompt, text = "Fever", variable= symptom_four_chk1_var)
symptom_four_chk1.place(x = 600, y = 530)

symptom_four_chk2_var = IntVar()
symptom_four_chk2 = Checkbutton(covid_prompt, text = "Cough", variable= symptom_four_chk2_var)
symptom_four_chk2.place(x = 600, y = 550)

symptom_four_chk3_var = IntVar()
symptom_four_chk3 = Checkbutton(covid_prompt, text = "Colds", variable= symptom_four_chk3_var)
symptom_four_chk3.place(x = 600, y = 570)

symptom_four_chk4_var = IntVar()
symptom_four_chk4 = Checkbutton(covid_prompt, text = "Muscle/body pains", variable= symptom_four_chk4_var)
symptom_four_chk4.place(x = 600, y = 590)

symptom_four_chk5_var = IntVar()
symptom_four_chk5 = Checkbutton(covid_prompt, text = "Sore Throat", variable= symptom_four_chk5_var)
symptom_four_chk5.place(x = 600, y = 610)

symptom_four_chk6_var = IntVar()
symptom_four_chk6 = Checkbutton(covid_prompt, text = "Diarrhea", variable= symptom_four_chk6_var)
symptom_four_chk6.place(x = 600, y = 630)

symptom_four_chk7_var = IntVar()
symptom_four_chk7 = Checkbutton(covid_prompt, text = "None of the above", variable= symptom_four_chk7_var)
symptom_four_chk7.place(x = 600, y = 650)

symptom_four_chk8_var = IntVar()
symptom_four_chk8 = Checkbutton(covid_prompt, text = "Headache", variable= symptom_four_chk8_var)
symptom_four_chk8.place(x = 820, y = 530)

symptom_four_chk9_var = IntVar()
symptom_four_chk9 = Checkbutton(covid_prompt, text = "Shortness of breath", variable= symptom_four_chk9_var)
symptom_four_chk9.place(x = 820, y = 550)

symptom_four_chk10_var = IntVar()
symptom_four_chk10 = Checkbutton(covid_prompt, text = "Difficulty of breathing", variable= symptom_four_chk10_var)
symptom_four_chk10.place(x = 820, y = 570)

symptom_four_chk11_var = IntVar()
symptom_four_chk11 = Checkbutton(covid_prompt, text = "Loss of taste", variable= symptom_four_chk11_var)
symptom_four_chk11.place(x = 820, y = 590)

symptom_four_chk12_var = IntVar()
symptom_four_chk12 = Checkbutton(covid_prompt, text = "Loss of smell", variable= symptom_four_chk12_var)
symptom_four_chk12.place(x = 820, y = 610)

# - Have you had exposure to probable or confirm case in the last 7 days?
covid_symptom_five = Label(covid_prompt, text = "Have you had exposure to probable or confirm case in the last 7 days?") 
covid_symptom_five.place(x = 600, y = 680)

symptom_five = IntVar()
covid_symptom_five_rbtn1 = Radiobutton(covid_prompt, text = "Yes", variable = symptom_five, value = "1")
covid_symptom_five_rbtn1.place(x = 600, y = 700)

covid_symptom_five_rbtn2 = Radiobutton(covid_prompt, text = "No", variable = symptom_five, value = "2")
covid_symptom_five_rbtn2.place(x = 600, y = 720)

# - Had contact with others with COVID Symptoms?
covid_symptom_six = Label(covid_prompt, text = "Have you had contact with others with COVID-19 Symptoms in the last 7 days?")
covid_symptom_six.place(x = 1100, y = 20)

symptom_six = IntVar()
covid_symptom_six_rbtn1 = Radiobutton(covid_prompt, text = "Yes", variable = symptom_six, value = "1")
covid_symptom_six_rbtn1.place(x = 1100, y = 40)

covid_symptom_six_rbtn2 = Radiobutton(covid_prompt, text = "No", variable = symptom_six, value = "2")
covid_symptom_six_rbtn2.place(x = 1100, y = 60)

# - Have you been tested for COVID-19 in the last 14 days?
covid_symptom_seven = Label(covid_prompt, text = "Have you been tested for COVID-19 in the last 14 days?") 
covid_symptom_seven.place(x = 1100, y = 100)

symptom_seven = IntVar()
covid_symptom_seven_rbtn1 = Radiobutton(covid_prompt, text = "Yes (Positive)", variable = symptom_seven, value = "1")
covid_symptom_seven_rbtn1.place(x = 1100, y = 120)

covid_symptom_seven_rbtn2 = Radiobutton(covid_prompt, text = "Yes (Negative)", variable = symptom_seven, value = "2")
covid_symptom_seven_rbtn2.place(x = 1100, y = 140)

covid_symptom_seven_rbtn3 = Radiobutton(covid_prompt, text = "No", variable = symptom_seven, value = "3")
covid_symptom_seven_rbtn3.place(x = 1100, y = 160)


#Additional Questions:
addtnl_question = Label(covid_prompt, text="Additional Questions")
addtnl_question.place(x= 1100 , y = 210 )

# - Most recent visited place
addtnl_one = Label(covid_prompt, text= "Most recent visited area/place?")
addtnl_one.place(x= 1100 , y = 230 )

addtnl_one_input = Entry(covid_prompt, width="30")
addtnl_one_input.place(x = 1100, y = 260)

# - Number of people you saw in the area
addtnl_two = Label(covid_prompt, text="Number of people you saw in the visited area/place?")
addtnl_two.place(x = 1100 , y = 290)

addtnl_two_input = Entry(covid_prompt, width="30")
addtnl_two_input.place(x = 1100, y = 310)

# - Mode of Transportation
addtnl_three = Label(covid_prompt, text="Mode of Transportation?")
addtnl_three.place(x = 1100, y = 340)

additional_three_qstn = IntVar()
addtnl_three_input  = Radiobutton(covid_prompt, text = "Public Transportation", variable = additional_three_qstn, value = "1")
addtnl_three_input.place(x = 1100, y = 360)

addtnl_three_input  = Radiobutton(covid_prompt, text = "Private Transportation", variable = additional_three_qstn, value = "2")
addtnl_three_input.place(x = 1100, y = 380)

# - Recent Medication Intake/Vitamin Intake
addtnl_four = Label(covid_prompt, text = "Recent Medication Intake / Vitamin Intake?")
addtnl_four.place(x = 1100, y = 420)

addtnl_four_input = Entry(covid_prompt, width = "30")
addtnl_four_input.place(x = 1100, y = 440)


# Submit Button:
submission_button = Button(covid_prompt, text ="Submit", width = "10", command = submit_records)
submission_button.place(x = 1150, y = 470)

# Last Message: Picture or Slogan Quote of Covid Safety Measures
from PIL import Image, ImageTk

img_message = "covid_poster.jpg"
image = Image.open(img_message)
img = ImageTk.PhotoImage(image)

img_message_input = Label(covid_prompt, image=img, width = "500", height= "400")
img_message_input.place(x=1100, y=550)

#Adding search entry to be able to look for keywords
identify_search = Entry(covid_prompt, width="30")
identify_search.place(x=1200, y=530)

scan_btn = Button(covid_prompt, text="Search", width="10", command = scan_covid_prompt_info)
scan_btn.place(x=1100, y=530)

covid_prompt.mainloop()