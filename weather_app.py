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

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    Weather().run()