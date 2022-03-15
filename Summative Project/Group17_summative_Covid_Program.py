# we are going to create covid-19 track record for a clinic

# Entity name: clinic
# Password: covid data storage

# this package will help us create Graphic User Interface(GUI) for our program
from tkinter import *

import os

# this package is with tkinter, it will help us create messageboxes for exception handling
from tkinter import messagebox as msgbox

from datetime import *  # this package will help us create dates in our program

from PIL import ImageTk, Image  # this package help us insert images in our program

# this package will help us create random number which will be used in creating unique code for patients
from random import *

root = Tk()     # initiate tkinter package
root.title("Covid-19 Test Records")  # create a title for our GUI
root.geometry("800x600")    # set size (height and width) for our GUI
root.resizable(width=None, height=None)

# insert an image on GUI
cover = ImageTk.PhotoImage(
    Image.open("C://Users//Admin//Desktop//CS Prog 1//Projects//Summative Project//Images//covid-19 image.png"))
my_image = Label(image=cover)  # create a label for our image
my_image.place(x=180, y=100)    # place that label on the screen of our GUI


class Password:  # create class password, it will handle the homepage GUI for our program
    # create label on our GUI
    entity_label = Label(root, text="Enter clinic name: ")
    # placed that label on our GUI
    entity_label.config(font=("Calibri bold", 15))
    entity_label.place(x=200, y=250)
    password_label = Label(root, text="Enter password: ")
    password_label.config(font=("Calibri bold", 15))
    password_label.place(x=200, y=300)

    global_testAge = 0     # this attributes will store variables which will be used in Testing
    global_testDate = 0    # this attributes will store variables which will be used in Testing
    # this attributes will store variables which will be used in Testing
    global_testMonth = 0
    global_testYear = 0  # this attributes will store variables which will be used in Testing
    global_testGender = ""
    global_testContact = 0

    def __init__(self):  # init method to declare our instance variables
        # created an entry on our GUI where user will input some data
        self.entity = Entry(root, width=20, font=("Calibri", 15))
        self.entity.place(x=380, y=250)  # placed that entry on our GUI screen
        # created another entry on our GUI where user will input password
        self.password = Entry(root, width=20, font=("calibri", 15))
        # placed that entry on our GUI screen
        self.password.place(x=380, y=300)
        # created a list where i will store data inputed in self.entity entry (to be used in testing)
        self.namelist = []
        # created a list where i will store password inputed in self.password (to be used in testing)
        self.passwordlist = []

    def enter(self):    # created a method, when user click on the a button that button will run codes in this method
        # append the data user inputed in the self.entity entry in the list
        self.namelist.append(self.entity.get())
        # append the password user inputed in the self.entity entry in the list
        self.passwordlist.append(self.password.get())

        # this condition will check if the user inputed the correct entries so that he can proceed to another page of the GUI
        if self.entity.get() == "clinic" and self.password.get() == "covid data storage":
            Password.entity_label.destroy()  # remove label on screen
            Password.password_label.destroy()   # remove label on screen
            self.entity.destroy()   # remove entry on screen
            self.password.destroy()  # remove entry on screen
            button_password.destroy()   # remove button on screen
            my_image.destroy()  # remove image on screen

            # created another class within the method enter because when user press the button to proceed on another page,
            # labels and entries which were on the page will be removed, in this class below it is where will create new labels and entries to input other data
            class Storage:
                page_title = Label(
                    root, text="Covid-19 Test Clinical Record Form")  # created label
                page_title.config(font=("Calibri bold", 20)
                                  )    # styled that label
                # placed that label on GUI screen
                page_title.place(x=200, y=25)

                title_label = Label(
                    root, text="Fill this record form")  # created label
                title_label.config(font=("Calibri bold", 13)
                                   )   # styled that label
                # placed that label on GUI screen
                title_label.place(x=200, y=65)

                clinic_label = Label(
                    root, text="Clinic name: ")    # created label
                # styled that label
                clinic_label.config(font=("Calibri bold", 13))
                # placed that label on GUI screen
                clinic_label.place(x=200, y=95)

                fname_label = Label(root, text="First name: ")
                fname_label.config(font=("calibri bold", 13))
                fname_label.place(x=200, y=128)

                lname_label = Label(root, text="Last name: ")
                lname_label.config(font=("calibri bold", 13))
                lname_label.place(x=200, y=161)

                gender_label = Label(root, text="Gender: ")
                gender_label.config(font=("calibri bold", 13))
                gender_label.place(x=200, y=194)

                ID_label = Label(root, text="ID number: ")
                ID_label.config(font=("calibri bold", 13))
                ID_label.place(x=200, y=227)

                nationality_label = Label(root, text="Nationality: ")
                nationality_label.config(font=("calibri bold", 13))
                nationality_label.place(x=200, y=260)

                dd_mm_yy_label = Label(root, text="Date of Birth: ")
                dd_mm_yy_label.config(font=("calibri bold", 13))
                dd_mm_yy_label.place(x=200, y=310)

                date_birth_label = Label(root, text="DD")
                date_birth_label.config(font=("calibri", 13))
                date_birth_label.place(x=310, y=285)

                month_birth_label = Label(root, text="MM")
                month_birth_label.config(font=("calibri", 13))
                month_birth_label.place(x=370, y=285)

                year_birth_label = Label(root, text="YY")
                year_birth_label.config(font=("calibri", 13))
                year_birth_label.place(x=430, y=285)

                age_label = Label(root, text="age: ")
                age_label.config(font=("calibri bold", 13))
                age_label.place(x=200, y=343)

                location_label = Label(root, text="Location: ")
                location_label.config(font=("calibri bold", 13))
                location_label.place(x=200, y=376)

                contact_label = Label(root, text="Contact: ")
                contact_label.config(font=("calibri bold", 13))
                contact_label.place(x=200, y=409)

                test_cite_label = Label(root, text="Test cite: ")
                test_cite_label.config(font=("calibri bold", 13))
                test_cite_label.place(x=200, y=442)

                def __init__(self):  # create init method to declare all instance variables
                    self.clinic = Entry(root, width=20, font=(
                        "calibri", 13))   # create an entry
                    # place that entry on GUI screen
                    self.clinic.place(x=300, y=95)

                    self.fname = Entry(root, width=20, font=(
                        "calibri", 13))    # create an entry
                    # place that entry on GUI screen
                    self.fname.place(x=300, y=128)

                    self.lname = Entry(root, width=20, font=(
                        "calibri", 13))    # create an entry
                    # place that entry on GUI screen
                    self.lname.place(x=300, y=161)

                    self.gender = Entry(root, width=20, font=(
                        "calibri", 13))   # create an entry
                    # place that entry on GUI screen
                    self.gender.place(x=300, y=194)

                    self.id = Entry(root, width=20, font=("calibri", 13))
                    self.id.place(x=300, y=227)

                    self.nationality = Entry(
                        root, width=20, font=("calibri", 13))
                    self.nationality.place(x=300, y=260)

                    self.date = Entry(root, width=5, font=("calibri", 13))
                    self.date.place(x=310, y=310)

                    self.month = Entry(root, width=5, font=("calibri", 13))
                    self.month.place(x=370, y=310)

                    self.year = Entry(root, width=5, font=("calibri", 13))
                    self.year.place(x=430, y=310)

                    self.age = Entry(root, width=20, font=("calibri", 13))
                    self.age.place(x=300, y=343)

                    self.location = Entry(root, width=20, font=("calibri", 13))
                    self.location.place(x=300, y=376)

                    self.contact = Entry(root, width=20, font=("calibri", 13))
                    self.contact.place(x=300, y=409)

                    self.cite = Entry(root, width=20, font=("calibri", 13))
                    self.cite.place(x=300, y=442)

                    self.count_1 = 0
                    self.count_2 = 0
                    self.count_3 = 0
                    self.count_4 = 0
                    self.count_5 = 0
                    self.count_6 = 0
                    self.count_7 = 0
                    self.count_8 = 0
                    self.count_9 = 0
                    self.count_10 = 0
                    self.count_11 = 0
                    self.count_12 = 0
                    self.record_storage = {     # create dictionary where to store data from all the entries we created
                        "clinic": [],
                        "first name": [],
                        "last name": [],
                        "gender": [],
                        "ID": [],
                        "nationality": [],
                        "date of birth": [],
                        "age": [],
                        "location": [],
                        "contact": [],
                        "test cite": [],

                    }

                # create another method, when user clicks a button to submit all that he/she inputed
                def storing(self):
                    # all the codes in this method will run to perform that task of submitting

                    clinic = self.clinic.get()  # stores data from the entry in the variable
                    first_name = self.fname.get()   # stores data from the entry in the variable
                    last_name = self.lname.get()    # stores data from the entry in the variable
                    gender = self.gender.get()
                    id_num = self.id.get()
                    nationality = self.nationality.get()
                    datebirth = self.date.get()
                    monthbirth = self.month.get()
                    yearbirth = self.year.get()
                    age = self.age.get()
                    location = self.location.get()
                    contact = self.contact.get()
                    test_cite = self.cite.get()

                    # this condition is need to show user that he/she needs to input every field of the form so that he/she can submit
                    if clinic == '' or first_name == '' or last_name == '' or gender == '' or id_num == '' or nationality == '' or datebirth == '' or monthbirth == '' or yearbirth == '' or age == '' or location == '' or test_cite == '' or contact == '':
                        msgbox.showwarning(
                            "Warning", "Input every field of the form!!!")  # this is message box will pop up to warn his/ sher

                    else:
                        try:    # handle an error when in gender input field user input incorrect answer required

                            # condition set so that user must enter in gender Male, Female, M or F
                            if gender == "Male" or gender == "Female" or gender == "M" or gender == "F":
                                # append every data of each input field in dictionary
                                self.record_storage["clinic"].append(clinic)
                                self.record_storage["first name"].append(
                                    first_name)  # append every data of each input field in dictionary
                                self.record_storage["last name"].append(
                                    last_name)  # append every data of each input field in dictionary
                                # append every data of each input field in dictionary
                                self.record_storage["gender"].append(gender)
                                self.record_storage["ID"].append(self.id.get())
                                self.record_storage["nationality"].append(
                                    nationality)
                                Password.global_testGender += "" + gender

                                try:    # handle an error when user inputs wrong data type in DATE input, as we need numbers
                                    DOB = date(int(yearbirth), int(
                                        monthbirth), int(datebirth))
                                    self.record_storage["date of birth"].append(
                                        str(DOB))   # after it is correct, it will append the date in the dictionary

                                    Password.global_testDate = int(datebirth)
                                    Password.global_testMonth = int(monthbirth)
                                    Password.global_testYear = int(yearbirth)

                                    try:    # handle an error when user input wrong data type in AGE and CONTACT input, as they are numbers
                                        # if this condition is true
                                        if type(int(age)) == int and type(int(contact)) == int:
                                            self.record_storage["age"].append(
                                                age)    # append age input in the dictionary
                                            self.record_storage["location"].append(
                                                location)   # append location input in the dictionary
                                            self.record_storage["contact"].append(
                                                contact)    # append contact input in the dictionary
                                            self.record_storage["test cite"].append(
                                                test_cite)

                                            Password.global_testAge = int(age)
                                            Password.global_testContact = int(
                                                contact)

                                            # this will print the dictionary in to see what data we inputed in every field
                                            print(self.record_storage)

                                            self.count_1 = len(
                                                self.record_storage["clinic"])
                                            self.count_2 = len(
                                                self.record_storage["first name"])
                                            self.count_3 = len(
                                                self.record_storage["last name"])
                                            self.count_4 = len(
                                                self.record_storage["gender"])
                                            self.count_5 = len(
                                                self.record_storage["ID"])
                                            self.count_6 = len(
                                                self.record_storage["nationality"])
                                            self.count_7 = len(
                                                self.record_storage["age"])
                                            self.count_8 = len(
                                                self.record_storage["location"])
                                            self.count_9 = len(
                                                self.record_storage["test cite"])
                                            self.count_10 = len(
                                                self.record_storage["date of birth"])
                                            self.count_11 = len(
                                                self.record_storage["contact"])

                                            # each time the user clicks the submit button, data needs to be removed in the input field so that he can input othe data
                                            # remove data in the input field
                                            self.clinic.delete(0, END)
                                            # remove data in the input field
                                            self.fname.delete(0, END)
                                            # remove data in the input field
                                            self.lname.delete(0, END)
                                            # remove data in the input field
                                            self.gender.delete(0, END)
                                            self.id.delete(0, END)
                                            self.nationality.delete(0, END)
                                            self.age.delete(0, END)
                                            self.location.delete(0, END)
                                            self.contact.delete(0, END)
                                            self.cite.delete(0, END)
                                            self.date.delete(0, END)
                                            self.month.delete(0, END)
                                            self.year.delete(0, END)

                                            # create a text file where all the data inputed will be stored
                                            file_line = open(
                                                "storage.txt", "r")
                                            global countLines, uniqueNumber
                                            rand1 = randint(0, 8)
                                            rand2 = randint(0, 9)
                                            rand3 = randint(0, 9)
                                            rand4 = randint(0, 9)
                                            # uniqueNumber = str(rand1) + str(rand2) + str(rand3) + str(rand4)
                                            countLines = 0
                                            for line in file_line:  # this loop will help us count number of line in our textfile
                                                countLines += 1

                                            file_line.close()

                                            # this is a random number which will change as we input different patient data
                                            # each patient in our storage log will be identified by a unique code
                                            uniqueNumber = "TEST" + str(
                                                rand1) + str(rand2) + str(rand3) + str(rand4) + str(countLines)
                                            # we opened again the text file in appending mode, then we will append everything from the GUI form input field
                                            file = open("Storage.txt", "a")
                                            file.write(
                                                "\n{} {:>25} {:>25} {:>25} {:>25} {:>25} {:>25} {:>25} {:>25} {:>25} "
                                                "{:>25} "
                                                "{:>25} {:>25}".format(
                                                    uniqueNumber,
                                                    self.record_storage[
                                                        "clinic"][
                                                        self.count_1 - 1],
                                                    self.record_storage[
                                                        "first name"][
                                                        self.count_2 - 1],
                                                    self.record_storage[
                                                        "last name"][
                                                        self.count_3 - 1],
                                                    self.record_storage[
                                                        "gender"][
                                                        self.count_4 - 1],
                                                    self.record_storage[
                                                        "ID"][
                                                        self.count_5 - 1],
                                                    self.record_storage[
                                                        "nationality"][
                                                        self.count_6 - 1],
                                                    self.record_storage[
                                                        "date of birth"][
                                                        self.count_10 - 1],
                                                    self.record_storage[
                                                        "age"][
                                                        self.count_7 - 1],
                                                    self.record_storage[
                                                        "location"][
                                                        self.count_8 - 1],
                                                    self.record_storage["contact"][self.count_11 - 1],
                                                    self.record_storage[
                                                        "test cite"][
                                                        self.count_9 - 1],
                                                    str(date.today())))

                                            # this is another GUI screen which pops up when user submits data from the form, it will tell him that data inputed has been stored successful
                                            # initiate our GUI screen
                                            result = Toplevel(root, bg="white")
                                            # size of the GUI screen
                                            result.geometry("300x300")
                                            image_s = Image.open(   # added an image in that GUI
                                                "C://Users//Admin//Desktop//CS Prog 1//Projects//Summative Project//Images//marked.png")
                                            image = ImageTk.PhotoImage(
                                                image_s.resize((300, 300), Image.ANTIALIAS))
                                            submit_image = Label(
                                                result, image=image)    # put the image in a label
                                            # place that image on GUI screen
                                            submit_image.place(x=1, y=1)
                                            result_label = Label(
                                                result, text="Results submitted!!!", bg="white")
                                            result_label.config(
                                                font=("calibri bold", 16))
                                            result_label.place(x=60, y=265)

                                            result.mainloop()   # closes the

                                            # this message box will pop up when you close all the GUI windows to tell where to find the data
                                            msgbox.showinfo(
                                                "Info", "check data stored in Storage.txt")

                                    except Exception:   # exception
                                        msgbox.showwarning(
                                            "Warning", "Age and Contact must be number")    # pop up message box to tell you where is the problem
                                        self.record_storage["clinic"].pop(0)
                                        self.record_storage["first name"].pop(
                                            0)
                                        self.record_storage["last name"].pop(0)
                                        self.record_storage["gender"].pop(0)
                                        self.record_storage["ID"].pop(0)
                                        self.record_storage["nationality"].pop(
                                            0)
                                        self.record_storage["date of birth"].pop(
                                            0)

                                except ValueError as e:  # exception
                                    # pop up message box to tell you where is the problem
                                    msgbox.showwarning("Warning", e)
                                    self.record_storage["clinic"].pop(0)
                                    self.record_storage["first name"].pop(0)
                                    self.record_storage["last name"].pop(0)
                                    self.record_storage["gender"].pop(0)
                                    self.record_storage["ID"].pop(0)
                                    self.record_storage["nationality"].pop(0)

                            else:
                                raise Exception(
                                    "Gender is Male(M) or Female(F)")
                        except Exception as error:  # exception
                            # pop up message box to tell you where is the problem
                            msgbox.showwarning("Warning", error)

            store = Storage()   # create object
            # create a button to submit data from the GUI form
            submit = Button(root, text="Submit", command=store.storing,
                            pady=10, padx=20, font=("Calibri bold", 15))    # button
            submit.place(x=300, y=480)  # style size of our button

        else:
            # message box pop up when user try so submit with missing info
            msgbox.showwarning("Warning", "Input correct name and password!!!")


security = Password()   # create an object

# create a button, this button is on the front page where you enter the name and password to proceed on the form
button_password = Button(root, text="Next", command=security.enter,
                         pady=10, padx=20, font=("Calibri bold", 15))
button_password.place(x=300, y=350)  # styled the size of the button

root.mainloop()  # closes the GUI interface

# when you close your GUI after inputing data, this code will open a notepad for you to see what you entered and stored
os.system("Storage.txt")
