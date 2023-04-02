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
        clock = Label(self.root, text = "2:30 pm", font = ("Helvetica", 30, 'bold'), 
                      fg = "white", bg = "#57adff")
        clock.place(x = 30, y = 20)


        timezone = Label(self.root, font = ("Helvetica", 20), fg = "white", bg = "#57adff")
        timezone.place(x = 600, y = 20)

        long_lat  = Label(self.root, font = ("Helvetica", 10), fg = "white", bg = "#57adff")
        long_lat.place(x = 600, y = 50)




    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    Weather().run()