import mysql.connector
import requests

mydb = mysql.connector.connect(
  host="survivalcraft.at",
  user="weather",
  passwd="RV7p7oGApi5YocEz",
  database="WeatherStation"
)

api_address='https://api.openweathermap.org/data/2.5/weather?id=7871710&appid=80a3973b72a4e1dac88160ca95b4d77d'
json_data = requests.get(api_address).json()
format_add = json_data['main']
print(json_data)

"""
mycursor = mydb.cursor()

sql = "INSERT INTO SensorData(Temperatur) VALUES (34.22)"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
"""