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

    
    def getWeather(self):
        city = self.textfield.get()

        geolocator = Nominatim(user_agent = "geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()

        result = obj.timezone_at(lng = location.longitude, lat = location.latitude)

        self.timezone.config(text = result)
        self.long_lat.config(text = f"{round(location.latitude, 2)}°N, {round(location.longitude, 2)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        self.clock.config(text = current_time)

        #weather 
        api = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&units=metric&appid=493d74e8eced6546b68c07d0db225984"
        json_data = requests.get(api).json()

        #current
        temp = json_data['list'][0]['main']['temp']
        humidity = int(json_data['list'][0]['main']['humidity'])
        pressure  = int(json_data['list'][0]['main']['pressure'])
        wind = json_data['list'][0]['wind']['speed']
        description = json_data['list'][0]['weather'][0]['description']
        
        self.t.config(text = (temp, "°C"))
        self.h.config(text = (humidity, "%"))
        self.p.config(text = (pressure,"hPa"))
        self.w.config(text = (wind, "m/s"))
        self.d.config(text = description)

        #print(len(json_data['list']))
        #print(json_data['list'][0]['dt_txt'])
        #print(json_data['list'][len(json_data['list'])-1]['dt_txt'])

        #first cell
        midnight_first = 0
        for i in range(len(json_data['list'])):
            if int(json_data['list'][i]['dt_txt'][11]) == 0 and int(json_data['list'][i]['dt_txt'][12]) == 0:
                midnight_first = i
                print(midnight_first)
                break
        
        firstdayimage = json_data['list'][0]['weather'][0]['icon']
        photo_1 = ImageTk.PhotoImage(file = f"icons/{firstdayimage}@2x.png")
        self.firstimage.config(image = photo_1)
        self.firstimage.image = photo_1

        tmpday1 = json_data['list'][0]['main']['temp']
        tmpnight1 = json_data['list'][midnight_first]['main']['temp']
        self.day1tmp.config(text = f"Day:{tmpday1}\n Night:{tmpnight1}")

        #second cell
        midday_second = 0
        midnight_second = 0
        x = False
        y = False
        for i in range(midnight_first + 1 ,len(json_data['list'])):
            if int(json_data['list'][i]['dt_txt'][11]) == 1 and int(json_data['list'][i]['dt_txt'][12]) == 2:
                midday_second = i
                print(midday_second)
                x = True
            if int(json_data['list'][i]['dt_txt'][11]) == 0 and int(json_data['list'][i]['dt_txt'][12]) == 0 and x == True:
                midnight_second = i
                print(midnight_second)
                y = True
            if x and y:
                break
        
        seconddayimage = json_data['list'][midday_second]['weather'][0]['icon'] #sprawdź indeksowanie ikon
        img = (Image.open(f"icons/{seconddayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo_2 = ImageTk.PhotoImage(resized_image)
        self.secondimage.config(image = photo_2)
        self.secondimage.image = photo_2

        tmpday2 = json_data['list'][midday_second]['main']['temp']
        tmpnight2 = json_data['list'][midnight_second]['main']['temp']
        self.day2tmp.config(text = f"Day:{tmpday2}\n Night:{tmpnight2}")

        #third cell
        
        midday_third = 0
        midnight_third = 0
        x = False
        y = False
        for i in range(midnight_second + 1, len(json_data['list'])):
            if int(json_data['list'][i]['dt_txt'][11]) == 1 and int(json_data['list'][i]['dt_txt'][12]) == 2:
                midday_third = i
                print(midday_third)
                x = True
            if int(json_data['list'][i]['dt_txt'][11]) == 0 and int(json_data['list'][i]['dt_txt'][12]) == 0 and x == True:
                midnight_third = i
                print(midnight_third)

                y = True
            if x and y:
                break
        
        thirddayimage = json_data['list'][midday_third]['weather'][0]['icon']
        img = (Image.open(f"icons/{thirddayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo_3 = ImageTk.PhotoImage(resized_image)
        self.thirdimage.config(image = photo_3)
        self.thirdimage.image = photo_3

        tmpday3 = json_data['list'][midday_third]['main']['temp']
        tmpnight3 = json_data['list'][midnight_third]['main']['temp']
        self.day3tmp.config(text = f"Day:{tmpday3}\n Night:{tmpnight3}")
        
        #fourth cell
        midday_fourth = 0
        midnight_fourth = 0
        x = False
        y = False
        for i in range(midnight_third + 1, len(json_data['list'])):
            if int(json_data['list'][i]['dt_txt'][11]) == 1 and int(json_data['list'][i]['dt_txt'][12]) == 2:
                midday_fourth = i
                print(midday_fourth)
                x = True
            if int(json_data['list'][i]['dt_txt'][11]) == 0 and int(json_data['list'][i]['dt_txt'][12]) == 0 and x == True:
                midnight_fourth = i
                print(midnight_fourth)
                y = True
            if x and y:
                break
    
        fourthdayimage = json_data['list'][midday_fourth]['weather'][0]['icon']
        img = (Image.open(f"icons/{fourthdayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo_4 = ImageTk.PhotoImage(resized_image)
        self.fourthimage.config(image = photo_4)
        self.fourthimage.image = photo_4
        
        tmpday4 = json_data['list'][midday_fourth]['main']['temp']
        tmpnight4 = json_data['list'][midnight_fourth]['main']['temp']
        self.day4tmp.config(text = f"Day:{tmpday4}\n Night:{tmpnight4}")

        #fifth cell
        midday_fifth = 0
        midnight_fifth = 0
        x = False
        y = False
        for i in range(midnight_fourth + 1 , len(json_data['list'])):
            if int(json_data['list'][i]['dt_txt'][11]) == 1 and int(json_data['list'][i]['dt_txt'][12]) == 2:
                midday_fifth = i
                print(midday_fifth)
                x = True
            if int(json_data['list'][i]['dt_txt'][11]) == 0 and int(json_data['list'][i]['dt_txt'][12]) == 0 and x == True:
                midnight_fifth = i
                print(midnight_fifth)
                y = True
            if x and y:
                break

        fifthdayimage = json_data['list'][midday_fifth]['weather'][0]['icon']
        img = (Image.open(f"icons/{fifthdayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo_5 = ImageTk.PhotoImage(resized_image)
        self.fifthimage.config(image = photo_5)
        self.fifthimage.image = photo_5

        tmpday5 = json_data['list'][midday_fifth]['main']['temp']
        tmpnight5 = json_data['list'][midnight_fifth]['main']['temp']
        self.day5tmp.config(text = f"Day:{tmpday5}\n Night:{tmpnight5}")
        
        
        #days
        first = datetime.now()
        self.day1.config(text = first.strftime("%A"))

        second = first + timedelta(days = 1)
        self.day2.config(text = second.strftime("%A"))

        third = second + timedelta(days = 1)
        self.day3.config(text = third.strftime("%A"))

        fourth = third + timedelta(days = 1)
        self.day4.config(text = fourth.strftime("%A"))

        fifth = fourth + timedelta(days = 1)
        self.day5.config(text = fifth.strftime("%A")) 


    def icons(self):

        self.image_icon = PhotoImage(file = "images/logo.png")
        self.root.iconphoto(False,self.image_icon)

        self.Round_box = PhotoImage(file = "images/Rounded Rectangle 1.png")
        Label(self.root,image = self.Round_box, bg = '#57adff').place(x = 30, y = 110)

        self.Search_image = PhotoImage(file = "images/Rounded Rectangle 3.png")
        self.myimage = Label(image = self.Search_image, bg = "#57adff")
        self.myimage.place(x = 270, y = 120)

        self.weat_image = PhotoImage(file = "images/Layer 7.png")
        self.weather_image = Label(self.root,image = self.weat_image, bg = "#203243")
        self.weather_image.place(x = 290, y = 127)

        self.textfield = tk.Entry(self.root, justify = "center", width = 15, 
                     font = ('poppins', 25, 'bold'), bg = "#203243", 
                     border = 0, fg = "white")
        self.textfield.place(x = 370, y = 130)
        self.textfield.focus()

        self.Search_icon = PhotoImage(file = "images/Layer 6.png")
        self.myimage_icon = Button(image = self.Search_icon, borderwidth = 0, cursor = "hand2", 
                              bg = "#203243", command = self.getWeather)
        self.myimage_icon.place(x = 645, y = 125)


    def labels(self):

        self.label1 = Label(self.root, text = "Temperature", font = ("Helvetica",11), fg = "white", bg = "#203243")
        self.label1.place(x = 40, y = 120)

        self.label2 = Label(self.root, text = "Humidity", font = ("Helvetica",11), fg = "white", bg = "#203243")
        self.label2.place(x = 40, y = 140)

        self.label3 = Label(self.root, text = "Pressure", font = ("Helvetica",11), fg = "white", bg = "#203243")
        self.label3.place(x = 40, y = 160)

        self.label4 = Label(self.root, text = "Wild Speed", font = ("Helvetica",11), fg = "white", bg = "#203243")
        self.label4.place(x = 40, y = 180)

        self.label5 = Label(self.root, text = "Description", font = ("Helvetica",11), fg = "white", 
                       bg = "#203243")
        self.label5.place(x = 40, y = 200)

        #thpwd
        self.t = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        self.t.place(x = 135, y = 120)

        self.h = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        self.h.place(x = 135, y = 140)

        self.p = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        self.p.place(x = 135, y = 160)

        self.w = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        self.w.place(x = 135, y = 180)

        self.d = Label(self.root, font = ("Helvetica", 11), fg = "white", bg = "#203243")
        self.d.place(x = 135, y = 200)


    def boxes(self):
        #Bottom box
        self.frame = Frame(self.root, width = 900, height = 180, bg = "#212120")
        self.frame.pack(side = BOTTOM)


        #Bottom boxes
        self.firstbox = PhotoImage(file = "images/Rounded Rectangle 2.png")
        self.secondbox = PhotoImage(file = "images/Rounded Rectangle 2 copy.png")

        Label(self.frame, image = self.firstbox, bg = "#212120").place(x = 30, y = 20)
        Label(self.frame, image = self.secondbox, bg = "#212120").place(x = 350, y = 30)
        Label(self.frame, image = self.secondbox, bg = "#212120").place(x = 475, y = 30)
        Label(self.frame, image = self.secondbox, bg = "#212120").place(x = 600, y = 30)
        Label(self.frame, image = self.secondbox, bg = "#212120").place(x = 725, y = 30)
    
    def clock(self):
        self.clock = Label(self.root, text = "2:30 pm", font = ("Helvetica", 30, 'bold'), 
                      fg = "white", bg = "#57adff")
        self.clock.place(x = 30, y = 20)


        self.timezone = Label(self.root, font = ("Helvetica", 20), fg = "white", bg = "#57adff")
        self.timezone.place(x = 600, y = 20)

        self.long_lat  = Label(self.root, font = ("Helvetica", 10), fg = "white", bg = "#57adff")
        self.long_lat.place(x = 600, y = 50)


    def first_cell(self):

        self.firstframe = Frame(self.root, width = 230, height = 132, bg = "#282829")
        self.firstframe.place(x = 35,y = 315)

        self.day1 = Label(self.firstframe, font ="arial 18", bg = "#282829", fg = "#fff")
        self.day1.place(x = 100, y= 5)

        self.firstimage = Label(self.firstframe, bg = "#282829")
        self.firstimage.place(x = 1, y = 15)

        self.day1tmp = Label(self.firstframe, bg = "#282829", fg = "#57adff", font = "arial 15 bold")
        self.day1tmp.place(x = 100, y = 50)

    def second_cell(self):
        
        self.secondframe = Frame(self.root, width = 70, height = 115, bg = "#282829")
        self.secondframe.place(x = 355,y = 325)

        self.day2 = Label(self.secondframe, bg = "#282829", fg = "#fff")
        self.day2.place(x = 5, y = 3)

        self.secondimage = Label(self.secondframe, bg = "#282829")
        self.secondimage.place(x = 7, y = 20)

        self.day2tmp = Label(self.secondframe, bg = "#282829", fg = "#fff")
        self.day2tmp.place(x = 2, y = 70)

    def third_cell(self):
        
        self.thirdframe = Frame(self.root, width = 70, height = 115, bg = "#282829")
        self.thirdframe.place(x = 480,y = 325)

        self.day3 = Label(self.thirdframe, bg = "#282829", fg = "#fff",  justify = CENTER)
        self.day3.place(x = 5, y = 3)

        self.thirdimage = Label(self.thirdframe, bg = "#282829")
        self.thirdimage.place(x = 7, y = 20)

        self.day3tmp = Label(self.thirdframe, bg = "#282829", fg = "#fff")
        self.day3tmp.place(x = 2, y = 70)

    def fourth_cell(self):
        
        self.fourthframe = Frame(self.root, width = 70, height = 115, bg = "#282829")
        self.fourthframe.place(x = 605, y = 325)

        self.day4 = Label(self.fourthframe, bg = "#282829", fg = "#fff",  justify = CENTER)
        self.day4.place(x = 5, y = 3)

        self.fourthimage = Label(self.fourthframe, bg = "#282829")
        self.fourthimage.place(x = 7, y = 20)

        self.day4tmp = Label(self.fourthframe, bg = "#282829", fg = "#fff")
        self.day4tmp.place(x = 2, y = 70)

    def fifth_cell(self):
        
        self.fifthframe = Frame(self.root, width = 70, height = 115, bg = "#282829")
        self.fifthframe.place(x = 730,y = 325)

        self.day5 = Label(self.fifthframe, bg = "#282829", fg = "#fff", justify = CENTER)
        self.day5.place(x = 5, y = 3)

        self.fifthimage = Label(self.fifthframe, bg = "#282829")
        self.fifthimage.place(x = 7, y = 20)

        self.day5tmp = Label(self.fifthframe, bg = "#282829", fg = "#fff")
        self.day5tmp.place(x = 2, y = 70)


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    Weather().run()