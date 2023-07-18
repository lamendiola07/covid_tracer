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

covid_prompt = tk.Tk()
covid_prompt.title("(CCT) Covid Contact Tracer - BetaTest v.0.0")
covid_prompt.geometry("1530x1530")

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

#Line Design to divide the main window

#Emergency Contact:
# -Name (First Name, Last Name)
name_emrgncy = Label(covid_prompt, text = "Name (First Name, Last Name):")
name_emrgncy.place(x = 600, y = 20)

name_emrgncy_input = Entry(covid_prompt, width ="30")
name_emrgncy_input.place(x = 600, y = 40)

# -Address:
address_emergncy = Label(covid_prompt, text = "Address:")
address_emergncy.place(x = 820, y= 20)

address_emergncy_input = Entry(covid_prompt, width ="30")
address_emergncy_input.place(x = 820, y = 40)

# -Contact Number/Landline
contact_emergncy = Label(covid_prompt, text = "Contact Number / Landline:")
contact_emergncy.place(x = 600, y = 80)

contact_emergncy_input = Entry(covid_prompt, width = "30")
contact_emergncy_input.place(x = 600, y = 100)

# -Email Address
email_emergncy = Label(covid_prompt, text ="E-mail Address:")
email_emergncy.place(x = 820, y = 80)

email_emergncy_input = Entry(covid_prompt, width ="30")
email_emergncy_input.place(x = 820, y = 100)

# -Relationship to the Contact Person
relationship_emergncy = Label(covid_prompt, text = "Relationship to the Contact Person:")
relationship_emergncy.place(x = 600, y = 130)

relationship_emergncy_input = Entry(covid_prompt, width="30")
relationship_emergncy_input.place(x =600, y = 150)


#Questions to Assure Covid Symptoms of User:
# - Have you been vaccinated for COVID-19?
# - What is the brand of your COVID-19 Vaccination
# - Are you experiencing symptoms in the past 7 days
# - Have you had exposure to probable or confirm case in the last 7 days?
# - Had contact with others with COVID Symptoms?
# - Have you been tested for COVID-19 in the last 14 days?


#Additional Questions:
# - Most recent visited place
# - Number of people you saw in the area
# - Mode of Transportation
# - Recent Medication Intake/Vitamin Intake

# Submit Button:
# Should ask user to confirm if the inputs are correct or not (Yes or No,Continue Editing)
# If Yes, End Program
# If Not, should be able to edit given data again

# Last Message: Picture or Slogan Quote of Covid Safety Measures

covid_prompt.mainloop()