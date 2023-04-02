from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


class Weather:
    
    def __init__(self):

        self.root = Tk()
        self.root.title("Weather app")
        self.root.geometry("890x470+300+300")
        self.root.resizable(False,False)
        self.root.configure(bg = "#57adff")
        
        self.icons()
        self.labels()
        self.boxes()
        self.clock()
        self.first_cell()
        self.second_cell()
        self.third_cell()
        self.fourth_cell()
        self.fifth_cell()

    

    def icons(self):

        image_icon = PhotoImage(file = "images/logo.png")
        self.root.iconphoto(False,image_icon)

        Round_box = PhotoImage(file = "images/Rounded Rectangle 1.png")
        Label(self.root,image = Round_box, bg = '#57adff').place(x = 30, y = 110)


    def labels(self):

        label1 = Label(self.root, text = "Temperature", font = ("Helvetica",11), fg = "white", bg = "#203243")
        label1.place(x = 40, y = 120)

        label2 = Label(self.root, text = "Humidity", font = ("Helvetica",11), fg = "white", bg = "#203243")
        label2.place(x = 40, y = 140)

        label3 = Label(self.root, text = "Pressure", font = ("Helvetica",11), fg = "white", bg = "#203243")
        label3.place(x = 40, y = 160)

        label4 = Label(self.root, text = "Wild Speed", font = ("Helvetica",11), fg = "white", bg = "#203243")
        label4.place(x = 40, y = 180)

        label5 = Label(self.root, text = "Description", font = ("Helvetica",11), fg = "white", 
                       bg = "#203243")
        label5.place(x = 40, y = 200)

        #thpwd
        t = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        t.place(x = 135, y = 120)

        h = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        h.place(x = 135, y = 140)

        p = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        p.place(x = 135, y = 160)

        w = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        w.place(x = 135, y = 180)

        d = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        d.place(x = 135, y = 200)


    def boxes(self):
        #Bottom box
        frame = Frame(self.root, width = 900, height = 180, bg = "#212120")
        frame.pack(side = BOTTOM)


        #Bottom boxes
        firstbox = PhotoImage(file = "images/Rounded Rectangle 2.png")
        secondbox = PhotoImage(file = "images/Rounded Rectangle 2 copy.png")

        Label(frame, image = firstbox, bg = "#212120").place(x = 30, y = 20)
        Label(frame, image = secondbox, bg = "#212120").place(x = 350, y = 30)
        Label(frame, image = secondbox, bg = "#212120").place(x = 475, y = 30)
        Label(frame, image = secondbox, bg = "#212120").place(x = 600, y = 30)
        Label(frame, image = secondbox, bg = "#212120").place(x = 725, y = 30)
    
    def clock(self):
        self.clock = Label(self.root, text = "2:30 pm", font = ("Helvetica", 30, 'bold'), 
                      fg = "white", bg = "#57adff")
        self.clock.place(x = 30, y = 20)


        timezone = Label(self.root, font = ("Helvetica", 20), fg = "white", bg = "#57adff")
        timezone.place(x = 600, y = 20)

        self.long_lat  = Label(self.root, font = ("Helvetica", 10), fg = "white", bg = "#57adff")
        self.long_lat.place(x = 600, y = 50)


    def first_cell(self):

        firstframe = Frame(self.root, width = 230, height = 132, bg = "#282829")
        firstframe.place(x = 35,y = 315)

        day1 = Label(firstframe, font ="arial 18", bg = "#282829", fg = "#fff")
        day1.place(x = 100, y= 5)

        firstimage = Label(firstframe, bg = "#282829")
        firstimage.place(x = 1, y = 15)

        day1tmp = Label(firstframe, bg = "#282829", fg = "#57adff", font = "arial 15 bold")
        day1tmp.place(x = 100, y = 50)

    def second_cell(self):
        
        secondframe = Frame(self.root, width = 70, height = 115, bg = "#282829")
        secondframe.place(x = 355,y = 325)

        day2 = Label(secondframe, bg = "#282829", fg = "#fff")
        day2.place(x = 5, y = 3)

        secondimage = Label(secondframe, bg = "#282829")
        secondimage.place(x = 7, y = 20)

        day2tmp = Label(secondframe, bg = "#282829", fg = "#fff")
        day2tmp.place(x = 2, y = 70)

    def third_cell(self):
        
        thirdframe = Frame(self.root, width = 70, height = 115, bg = "#282829")
        thirdframe.place(x = 480,y = 325)

        day3 = Label(thirdframe, bg = "#282829", fg = "#fff",  justify = CENTER)
        day3.place(x = 5, y = 3)

        thirdimage = Label(thirdframe, bg = "#282829")
        thirdimage.place(x = 7, y = 20)

        day3tmp = Label(thirdframe, bg = "#282829", fg = "#fff")
        day3tmp.place(x = 2, y = 70)

    def fourth_cell(self):
        
        fourthframe = Frame(self.root, width = 70, height = 115, bg = "#282829")
        fourthframe.place(x = 605, y = 325)

        day4 = Label(fourthframe, bg = "#282829", fg = "#fff",  justify = CENTER)
        day4.place(x = 5, y = 3)

        fourthimage = Label(fourthframe, bg = "#282829")
        fourthimage.place(x = 7, y = 20)

        day4tmp = Label(fourthframe, bg = "#282829", fg = "#fff")
        day4tmp.place(x = 2, y = 70)

    def fifth_cell(self):
        
        fifthframe = Frame(self.root, width = 70, height = 115, bg = "#282829")
        fifthframe.place(x = 730,y = 325)

        day5 = Label(fifthframe, bg = "#282829", fg = "#fff", justify = CENTER)
        day5.place(x = 5, y = 3)

        fifthimage = Label(fifthframe, bg = "#282829")
        fifthimage.place(x = 7, y = 20)

        day5tmp = Label(fifthframe, bg = "#282829", fg = "#fff")
        day5tmp.place(x = 2, y = 70)


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    Weather().run()