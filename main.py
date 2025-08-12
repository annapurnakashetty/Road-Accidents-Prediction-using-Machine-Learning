import numpy as np 
import pandas as pd 
data=pd.read_csv(“accident.csv”) 
df.head()
df.describe()
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
accidents_df = pd.read_csv(‘accident.csv') 
reason_counts = accidents_df['Reason'].value_counts() 
colors = plt.cm.Spectral(np.linspace(0, 1, len(reason_counts))) 
plt.figure(figsize=(8,8))  
plt.pie(reason_counts, labels=reason_counts.index, colors=colors, autopct='%1.1f%%', startangle=90) 
plt.title('Reasons for Accidents', fontsize=18) 
plt.axis('equal') 
plt.show()
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 
accidents_df = pd.read_csv('accident.csv') 
state_accidents = accidents_df.groupby('State')['Accident_ID'].count().reset_index() 
sorted_states = state_accidents.sort_values(by='Accident_ID', ascending=False) 
top_states = sorted_states.head(10) 
colors = cm.Spectral(top_states['Accident_ID'] / float(max(top_states['Accident_ID']))) 
plt.barh(top_states['State'], top_states['Accident_ID'], color=colors) 
plt.title('Number of Accidents by State (Top 10)') 
plt.xlabel('Number of Accidents') 
plt.ylabel('State') 
plt.show()
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 
accidents_df = pd.read_csv('accident.csv') 
weather_accidents = accidents_df.groupby('Weather_Conditions')
 ['Accident_ID'].count().reset_index() 
sorted_weather = weather_accidents.sort_values(by='Accident_ID', ascending=False) 
top_weather = sorted_weather.head(10) 
colors = cm.Spectral_r(top_weather['Accident_ID']/float(max(top_weather['Accident_ID']))) 
plt.bar(top_weather['Weather_Conditions'], top_weather['Accident_ID'], color=colors) 
plt.title('Number of Accidents by Weather Condition') 
plt.xlabel('Weather Condition') 
plt.ylabel('Number of Accidents') 
plt.show()
import pandas as pd 
import matplotlib.pyplot as plt 
accidents_df = pd.read_csv('accident.csv', usecols=['Speed_Limit', 'Number_of_Deaths']) 
speed_stats = accidents_df.groupby('Speed_Limit', as_index=False)['Number_of_Deaths'].mean() 
plt.plot(speed_stats['Speed_Limit'], speed_stats['Number_of_Deaths'], label='Average Number of 
Deaths') 
plt.title('Impact of Speeding on Accident Severity') 
plt.xlabel('Speed Limit') 
plt.ylabel('Average Number of Deaths/Injuries') 
plt.legend() 
plt.show()
import pandas as pd 
import matplotlib.pyplot as plt 
accidents_df = pd.read_csv('accident.csv') 
alcohol_accidents_df = accidents_df[accidents_df['Alcohol_Involved'] == 'Yes'] 
state_counts = alcohol_accidents_df['State'].value_counts() 
plt.bar(state_counts.index, state_counts.values, color=plt.cm.Spectral(state_counts.values/
 max(state_counts.values))) 
plt.title('Alcohol-Related Accidents by State') 
plt.xlabel('State') 
plt.ylabel('Number of Accidents') 
plt.xticks(rotation=90, fontsize=8) 
plt.show()
import pandas as pd 
import matplotlib.pyplot as plt 
accidents_df = pd.read_csv('accident.csv') 
accidents_df['Location_Type'] = accidents_df['Road_Type'].apply(lambda x: 'Rural' if 
x.startswith('R') else 'Urban') 
location_counts = accidents_df['Location_Type'].value_counts() 
colors = ['#ff7f0e', '#1f77b4'] 
plt.pie(location_counts.values, labels=location_counts.index, colors=colors, autopct='%1.1f%%') 
plt.title('Accidents by Location Type') 
plt.show()
import os 
import secrets 
import time 
from twilio.rest import Client 
account_sid = "AC00709cd49b7b8b39ff08b38420b6508a" 
auth_token = "6f4b2d849b1a7787da5b687fe17e66bb" 
client = Client(account_sid, auth_token) 
from_number = "+16205071602" 
to_number = "+919492333588" 
alcohol_input = input("Have you consumed alcohol? (yes/no) ").lower() 
if alcohol_input == "yes": 
    alcohol_detected = True 
else: 
    alcohol_detected = False 
    def generate_key(length): 
        return secrets.token_hex(length//2) 
    def generate_captcha(): 
        captcha = generate_key(6) 
        print(f"Captcha: {captcha}") 
        return captcha 
    def check_answer(answer, key): 
        return answer == key 
max_attempts = 3 
    attempts = 0 
    while attempts < max_attempts: 
        captcha_key = generate_captcha() 
        user_answer = input("Enter the captcha: ")
 18
if check_answer(user_answer, captcha_key): 
            print("Success! Captcha matches the key.") 
            break 
        else: 
            attempts += 1 
            if attempts == max_attempts: 
                print("Error! Three wrong attempts, driver has consumed alcohol.") 
                alcohol_detected = True 
            else: 
                print(f"Error! Captcha does not match the key. {max_attempts - attempts} attempts 
remaining.") 
speed_input = input("Enter your current speed (km/h): ") 
speed = int(speed_input) 
if speed > 100 : 
    message_body = f"Your Companion is overspeeding and Speed is {speed_input} km/h." 
    message = client.messages.create( 
        body=message_body, 
        from_=from_number, 
        to=to_number 
    ) 
    print("You are overspeeding, Message sent to your registered mobile number. ") 
if alcohol_detected: 
    message_body = f"Your Companion has consumed alcohol and is trying to drive the car. Please send 
emergency services." 
    message = client.messages.create( 
        body=message_body, 
        from_=from_number,
 to=to_number 
    ) 
    print("You have consumed alcohol , Message sent to your registered mobile number. ") 
if speed > 100 and alcohol_detected: 
    message_body = f"Your Companion is overspeeding and Speed is {speed_input} km/h and has 
consumed alcohol. Please send emergency services." 
    message = client.messages.create( 
        body=message_body, 
        from_=from_number, 
        to=to_number 
    ) 
print("You have consumed alcohol and also overspeedning, Message sent to your registered 
mobile number. ") 
    print("Message SID:", message.sid) 
else: 
    print("You are driving safely”) 
print("You have consumed alcohol and also overspeedning, Message sent to your registered 
mobile number. ") 
    print("Message SID:", message.sid) 
else: 
    print("You are driving safely”)