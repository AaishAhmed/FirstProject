# API Key from: openweathermap.org/api
key = "8ca541a16d5408434ea4728058eda210"

# IMPORTANT: If code not working, make sure to enter:
# "pip install requests" without quotations into command prompt

#TODO:
#Fix recheck: Error with wish inputs when input is invalid

import requests

print()
print("Welcome to the Weather App! Type 'quit' to quit at any time.")

def find_city():
    cityL = input("Please enter a city (Ex: Toronto) : ")

    if cityL == 'quit':
        print("Closing Program...")
        quit()
    else:
        pass

    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityL}&units=metric&APPID={key}")
    if data.status_code == 404:
        print("Invalid input, please try again.")
        find_city()
    else:
        return(cityL)

city = find_city()

#Sending request and receiving data using API
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}")


#print(data.json())

print()
print("City Found! For a list of available inputs, enter 'help'.")

def recheck(city, data):
    option_stat = input("Would you like to check a different statistic? ")
    if option_stat.lower() == "yes":
        wish(city, data)
    elif option_stat.lower() == "no":
        
        option_city = input("Okay, would you like to check the weather elsewhere? ")
        if option_city.lower() == "yes":
            city = find_city()
            #Sending request and receiving data using API
            data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}")


            #print(data.json())

            print()
            print("City Found! For a list of available inputs, enter 'help'.")
            wish(city, data)
        elif option_city.lower() == "no":
            print("Thanks for using the Weather App!")
            quit()
        else:
            print("Invalid input, please try again.")
            recheck(city, data)

    else:
        print("Invalid input, please try again.")
        recheck(city, data)


def wish(city, data):
    info = input("What would you like to know about the weather? ")

    if info.lower() == "help":
        print("Available inputs: 'sky', 'temp' or 'tempurature', 'wind'.")
        print()
        wish(city, data)

    elif info.lower() == "sky":
        clouds = data.json()['weather'][0]['main']

        if "clear" in clouds.lower():
            print("It seems to be", clouds.lower(), "in", city, "today.")
        else:
            print("There seems to be", clouds.lower(), "in", city, "today.")

        print()
        recheck(city, data)

    elif info.lower() == "tempurature" or  info.lower() == "temp":
        actualTemp = int(data.json()['main']['temp'])
        min = int(data.json()['main']['temp_min'])
        max = int(data.json()['main']['temp_max'])
        feels = int(data.json()['main']['feels_like'])

        print("The tempurature in", city, "is", actualTemp, "°C, feels like", feels, "°C, and will range from ", min, "°C and", max, "°C.")
        print()
        recheck(city, data)

    elif info.lower() == "wind":
        speed = data.json()['wind']['speed']
        direction = data.json()['wind']['deg']

        if 337.5 <= direction < 22.5 or (337.5 <= direction <= 360) or (0 <= direction < 22.5):
            direction = "N"
        elif 22.5 <= direction < 67.5:
            direction = "NE"
        elif 67.5 <= direction < 112.5:
            direction = "E"
        elif 112.5 <= direction < 157.5:
            direction = "SE"
        elif 157.5 <= direction < 202.5:
            direction = "S"
        elif 202.5 <= direction < 247.5:
            direction = "SW"
        elif 247.5 <= direction < 292.5:
            direction = "W"
        elif 292.5 <= direction < 337.5:
            direction = "NW"
        else:
            direction = "Error Detected" 
        
        print("Winds in", city, "are at", speed, "kph towards the", direction,)
        print()
        recheck(city, data)

    elif info.lower() == "quit":
        print("Closing program...")
        quit()

    else:
        print("Sorry, the input was invalid. Please try again.")
        wish(city, data)

wish(city, data)

