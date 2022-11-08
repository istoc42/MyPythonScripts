import requests
import urllib3
from datetime import datetime
import smtplib
import time

urllib3.disable_warnings()

MY_EMAIL = "shudso91@gmail.com"
MY_PASSWORD = "Hexblade4!"
MY_LAT = 51.505890
MY_LONG = -2.590060

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"] )
iss_longitude = float(data["iss_position"]["longitude"])
iss_current_position = (iss_latitude, iss_longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# print(f'The current position of the ISS is {iss_current_position}')
# print(f'My current position is {(MY_LAT, MY_LONG)}')

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
sunset = int(data["results"]["sunset"].split('T')[1].split(":")[0])
time_now = str(datetime.now())
current_hour = int(time_now.split(' ')[1].split(':')[0])

# print(f'Sunrise hour: {sunrise}')
# print(f'Sunset hour: {sunset}')
# print(f'Current hour: {current_hour}')

def is_night():
    #If it's day time, return true.
    if current_hour >= sunset and current_hour <= sunrise:
        return True

def is_iss_overhead():
    # Check if the ISS position is within 5 degrees of my position
    if MY_LAT - 5 <= iss_latitude or MY_LAT + 5 >= iss_latitude:
        print("ISS Lat OK")
        if MY_LONG - 5 <= iss_longitude  or MY_LAT + 5 >= iss_longitude  :
            print("ISS Long OK")
            print("LOOK UP!")
            return True
        else:
            print("ISS Long fail")
    else:
        print("ISS Lat fail")

# Check if it is night time
if is_night() == False:
    is_iss_overhead()
else:
    print("It is day time, my dudes. You can't see the ISS right now.")
        
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up!\n\nThe ISS is above you in the sky."
        )


# https://api.sunrise-sunset.org/json?lat=51.505890&long=-2.590060

