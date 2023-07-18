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
covid_prompt = Tk()
covid_prompt.title("(CCT) Covid Contact Tracer - BetaTest v.0.0")
covid_prompt.geometry("500x500")
covid_prompt.mainloop()


#Message before Form: "Fill out the form with outmost honesty for safety measures and well being of others. Maraming Salamat Po!"

#Form for Asking Personal Questions:
# - Name: (First Name, Middle Name, Last Name)
# - Address: (Current & Permanent)
# - Birthdate:
# - Contact Number/Landline:
# - Email Address:
# - Civil Status:
# - Religion:
# - Occupation:
# - Workplace Name/ School or University Name:
# - Workplace Address / School or University Address

#Emergency Contact:
# -Name (First Name, Last Name)
# -Address:
# -Contact Number/Landline
# -Email Address
# -Relationship to the Contact Person

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

# Last MEssage: Picture or Slogan Quote of Covid Safety Measures



