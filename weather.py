import tkinter as tk
import requests
import time

def getWeather(canvas):
    lat = textfield1.get()
    lon = textfield2.get()
    api = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=1967522e244a31341440abeb65cd82c8"
    json_data = requests.get(api).json()
    place = json_data['name']
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 37800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 37800))

    final_info = condition + "\n" + str(temp) + " C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + " C" + "\n" + "Min Temp: " + str(min_temp) + " C" + "\n" + "Pressure: " + str(pressure) + " hPa" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Wind Speed: " + str(wind) + " m/s" + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    place_label.config(text = place)
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x700")
canvas.title("Ben's Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

lat_label = tk.Label(canvas, font = f, text = "Enter Latitude:")
lat_label.pack(pady = 10)
textfield1 = tk.Entry(canvas, font = t)
textfield1.pack(pady = 10)
textfield1.focus()

lon_label = tk.Label(canvas, font = f, text = "Enter Longitude:")
lon_label.pack(pady = 10)
textfield2 = tk.Entry(canvas, font = t)
textfield2.pack(pady = 10)
textfield2.bind('<Return>', getWeather)

place_label = tk.Label(canvas, font = f)
place_label.pack(pady = 10)
label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()