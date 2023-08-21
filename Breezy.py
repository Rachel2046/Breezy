from tkinter import Tk, Label, Button, Entry, NE, StringVar
import requests
import time


class Breezy:

    def __init__(self, master):
        self.master = master
        master.title("Breezy")
        self.city = ''

        self.coordinates = StringVar()
        self.coordinates.set('')
        self.coordinates_content = Label(master, textvariable=self.coordinates)

        self.localtime = StringVar()
        self.localtime.set('')
        self.localtime_content = Label(master, textvariable=self.localtime)

        self.weather = StringVar()
        self.weather.set('')
        self.weather_content = Label(master, textvariable=self.weather)

        self.hilow = StringVar()
        self.hilow.set('')
        self.hilow_content = Label(master, textvariable=self.hilow)

        self.temperature = StringVar()
        self.temperature.set('')
        self.temperature_content = Label(master, textvariable=self.temperature)

        self.feelslike = StringVar()
        self.feelslike.set('')
        self.feelslike_content = Label(master, textvariable=self.feelslike)

        self.humidity = StringVar()
        self.humidity.set('')
        self.humidity_content = Label(master, textvariable=self.humidity)

        self.error = StringVar()
        self.error.set('')
        self.error_content = Label(master, textvariable=self.error, fg='#f00')

        self.prompt_label = Label(master, text="Type in city name to check the weather there...")
        self.coordinates_label = Label(master, text="City location:")
        self.localtime_label = Label(master, text="Local time:")
        self.weather_label = Label(master, text="Weather:")
        self.hilow_label = Label(master, text="Low~Hi (°C):")
        self.temperature_label = Label(master, text="Temperature right now:")
        self.feelslike_label = Label(master, text="Feels like:")
        self.humidity_label = Label(master, text="Humidity:")

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.checkweather_button = Button(master, text="Check weather", command=self.check_weather)

        # LAYOUT
        top_space = 50
        self.prompt_label.place(x=50, y=top_space-20)
        self.entry.place(x=50, y=top_space, width=150)
        self.checkweather_button.place(x=300, y=top_space, anchor=NE)

        self.coordinates_label.place(x=50, y=top_space+30)
        self.coordinates_content.place(x=300, y=top_space+30, anchor=NE)

        self.localtime_label.place(x=50, y=top_space+50)
        self.localtime_content.place(x=300, y=top_space+50, anchor=NE)

        self.weather_label.place(x=50, y=top_space+70)
        self.weather_content.place(x=300, y=top_space+70, anchor=NE)

        self.hilow_label.place(x=50, y=top_space+90)
        self.hilow_content.place(x=300, y=top_space+90, anchor=NE)

        self.temperature_label.place(x=50, y=top_space+110)
        self.temperature_content.place(x=300, y=top_space+110, anchor=NE)

        self.feelslike_label.place(x=50, y=top_space+130)
        self.feelslike_content.place(x=300, y=top_space+130, anchor=NE)

        self.humidity_label.place(x=50, y=top_space+150)
        self.humidity_content.place(x=300, y=top_space+150, anchor=NE)

        self.error_content.place(x=50, y=top_space + 170)

    def validate(self, new_text):
        self.city = new_text
        return True

    def check_weather(self, event=None):
        api_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': self.city,
            # Apply for a free API key from openweathermap.org
            'appid': 'your_free_api_key_from_openweathermap.org',
            'units': 'metric'
        }

        res = requests.get(api_url, params=params)

        data = res.json()
        if data['cod'] == 200:
            self.error.set('')
            weather = data['weather'][0]['description']
            hilow = f"Hi: {data['main']['temp_max']}, Low: {data['main']['temp_min']}"
            temperature = data['main']['temp']
            feelslike = data['main']['feels_like']
            humidity = data['main']['humidity']
            gmt = time.gmtime()
            localtime = f"{data['timezone'] // 3600 + gmt.tm_hour}:{gmt.tm_min}"

            self.coordinates.set(f"Lat: {data['coord']['lat']}, Longi: {data['coord']['lon']}")
            self.localtime.set(localtime)
            self.weather.set(weather)
            self.hilow.set(hilow)
            self.temperature.set(temperature)
            self.feelslike.set(feelslike)
            self.humidity.set(f"{humidity}%")
        else:
            self.coordinates.set('')
            self.localtime.set('')
            self.weather.set('')
            self.hilow.set('')
            self.temperature.set('')
            self.feelslike.set('')
            self.humidity.set('')
            self.error.set("Something went wrong, try again...")


root = Tk()
root.geometry('350x250')
my_gui = Breezy(root)
root.bind('<Return>', my_gui.check_weather)
root.iconbitmap('Breezy.ico')
root.mainloop()
