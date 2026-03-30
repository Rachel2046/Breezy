# `Breezy`: instantaneous weather report around the globe

`Breezy` is a Python + Tkinter Windows app that lets you check the weather anywhere in the world instantaneously.

## How to run it
In Windows, simply:
1) Double click the orange icon with the letter B, ![Icon of Breezy](doc/Breezy_icon.png) this runs `Breezy.exe`. Make sure you have `Breezy.ico` (the icon image) in the same folder, or you'll get the `"Breezy.ico" not defined` error... 
2) In the main window, type the name of the city you are interested in... Voila!
3) You will get the location (longitude and latitude), current time, weather and temperature instantaneously!
   
![Window example of Breezy](doc/Breezy_window.png)

## Check the source code
The Python code is also included. Feel free to modify the code and make your own version of `Breezy`... As `Breezy` is calling a public API from https://api.openweathermap.org/data/2.5/weather, you will need to apply for your own API key at `https://openweathermap.org/api` for free. Once you add your API key to the following section of the code in Breezy.py, you can query the server 60 times per minute or 1,000,000 times per month!

```python
params = {
            'q': self.city,
            # Apply for a free API key from openweathermap.org
            'appid': 'your_free_api_key_from_openweathermap.org',
            'units': 'metric'
        }
```
## From Tkinter to .exe
Having a Tkinter app is great, but what's the point of having a cool little weather tool if you can't share it with your friends? This website (https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/) has one of the best tutorials for converting your Tkinter applications to an executable so anyone can run it in Windows. Just to share what I did for Breezy (after installing `pyinstaller`):

```
pyinstaller --noconsole --onefile --icon=Breezy.ico Breezy.py
```

## Fun fact
Try type in `1234` for the city name, see what happens 😉
