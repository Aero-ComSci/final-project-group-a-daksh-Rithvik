import requests
api_key = '30d4741c779ba94c470ca1f63045390a'
lucky_city = ["los angeles", "dublin", "pleasanton", "miami", "durham")
city = input("Which City Weather Would You Like To Know: ").lower()
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&APPID=" + api_key)
data = response.json()

if data['cod'] == '404':
  print("City Not Found")
else:
  print("Weather: " + data['weather'][0]['main'])
  print("Temperature: " + str(round(data['main']['temp'])) + 'F')
  if city in lucky_city:
    print("Congratulations! You are the lucky winner!!!")
    print("You get a Free Ice Cream")
