# Alarm-Clock-Python :watch:
A simple Alarm Clock in Python (24hr, No GUI). Python libraries used: datetime, time, winsound

## Thoughts on starting this project
My fifth programming project, in Python. 

I wanted to explore different libraries present in Python. The idea came up when looking at how people made an alarm clock project in Python and realising they
are importing libraries with commands I had no idea how to use, like datetime, time and winsound.

I started by learning through practicing with Youtube tutorials on the individiaul libraries, then bringing them together to make this Alarm Clock project. Well
of course, with inspiration online, even though many of them had a GUI function (with tkinter library) with it, when I wanted to make a non-GUI one first.

<br>

Computer program used for coding: VS Code

## Code description
Let's start with:
1. Imported Libraries
2. Global variables
3. Self-defined functions
4. Main code

<br>

<br>

**1. Imported Libraries**
```python
import datetime
import winsound
import time
```
Yay! More libraries other than the 'random' library. :rofl:

<br>

<br>

**2. Global variables**
```python
global datetime_today
datetime_today = datetime.datetime.today()
```
Gets date and time of the present time (year, month, day, hours, minutes, second, microsecond). If keeps refreshing the variable will keep changing.

<br>

```python
global datetime_today_string
datetime_today_string = datetime_today.strftime("%B %d %Y %H:%M:%S")
```
Converting the output of 'datetime_today' to become more readible in format of e.g. February 18 2023 16:27:58. Else it will look like 
2023-02-18 16:27:58.804579.

(Self-note: strftime converts datetime to string, while strptime converts string to datetime)

<br>

```python
global date_today
date_today = datetime.date.today()
```
Gets only the date of the present time (year, month, day). If keeps refreshing the variable will keep changing.

<br>

<br>

**3. Self-defined functions**
```python
def alarm_countdown(n):
    while True:
        current_time = datetime.datetime.today().replace(microsecond=0)
        time.sleep(1)
        print(f"{current_time}, {n}")

        if n == current_time:
            print("Alarm ringing!!")
            winsound.PlaySound("defaultsound", winsound.SND_ASYNC + winsound.SND_LOOP)
            break
```
The 'alarm_countdown(n)' function is for the ending part of the main code. This function takes 1 argument, the datetime where the user has set his/her alarm.
It then creates a while loop which will print out the current time every 1 second (using time.sleep(1)), and comparing it to the time set by user.
'.replace(microsecond=0)' is used to remove the microsecond parameter in 'datetime.datetime.today()' so that 'datetime.datetime.today()' can eventually be equal
to datetime set by user, which does not have microsecond parameter.

When 'datetime.datetime.today()' == datetime set by user, n, the winsound.Playsound will run (infinitely due to the loop) and will play the default sound 
(as I did not add a soundtrack into the file in Github), until the user puts an input to stop the sound. (this code is in the main code)

<br>

```python
def user_input_date_year():
    while True:
        try:
            x = int(input("Year: "))
            if x >= datetime_today.year and x < 2101:
                break
        except:
            print("Please type in a valid year! (up to year 2100)")
    return x

def user_input_date_month():
    while True:
        try:
            x = int(input("Month: "))
            if x > 0 and x < 13:
                break
        except:
            print("Please type in a valid year! (1 to 12)")
    return x

def user_input_date_day():
    while True:
        try:
            x = int(input("Day: "))
            if x > 0 and x < 32:
                break
        except:
            print("Please type in a valid day! (1 to 31)")
    return x

def user_input_date_hours():
    while True:
        try:
            x = int(input("Hour: "))
            if x > -1 and x < 24:
                break
        except:
            print("Please type in a valid number! (between 1 to 59)")
    return x
        
def user_input_date_mins():
    while True:
        try:
            x = int(input("Min: "))
            if x > -1 and x < 60:
                break
        except:
            print("Please type in a valid number! (between 1 to 59)")
    return x

def user_input_date_secs():
    while True:
        try:
            x = int(input("Sec: "))
            if x > -1 and x < 60:
                break
        except:
            print("Please type in a valid number! (between 1 to 59)")
    return 
```
These functions gets the respective parameters for the user's set datetime (year, month, day, hours, minutes, second), and checks if the user's input make sense
in the context. e.g. Year must be an int, up till 2100, and must be larger than the present year. Month must be a number between 1 to 12. 
Minutes must be a number from 1 to 59.

<br>

<br>

**4. Main code**
```python
print("Welcome to Simple Alarm Clock! (24hour, no GUI)")
print(f"Current date and time: {datetime_today_string}")
print("")
time.sleep(2)
```
Aesthetics for the code. Gives current datetime for the user to reference to when setting their alarm clock. Sleeps for 2 seconds so the code is user-friendly and
easier to follow.

<br>

```python
def main(): 
    while True:
        try:
            print("Please select the date you would like the alarm to go off:")
            a = user_input_date_year()
            b = user_input_date_month()
            c = user_input_date_day()

            dt_alarmtest = datetime.date(a, b, c)
```
This first while loop gets the date parameters for the user's set datetime. Makes it into a date object, 'dt_alarmtest'. 
            
<br>
            
```python
            date_diff = dt_alarmtest - date_today 
            
            tdelta = datetime.timedelta(days=0)

            if date_diff >= tdelta:
                break
        except:
            print("Please re-enter the date!")
```
Now to check if date set is logical. If date set is in the past (if tdelta (datetime difference) is a negative number), then the user is re-prompted to reset their date. Else,
they break out of the first while loop and proceeds.

<br>

```python
    while True:
        try:
            print("Please select the time you would like the alarm to go off (24hr clock):")
            x = user_input_date_hours()
            y = user_input_date_mins()
            z = user_input_date_secs()
```
This second while loop gets the time parameters for the user's set datetime. Makes it into a date object, 'dt_diff'.

<br>

```python
            time_set = datetime.datetime(a, b, c, x, y, z)

            dt_diff = time_set - datetime.datetime.today()
            if dt_diff >= tdelta:
                break
        except:
            print("Please re-enter the time!")
```
Similarly, we now check if time set is logical. Combining with the date, which we now know must be logical, if datetime set is in the past (if 
tdelta (datetime difference) is a negative number), then the user is re-prompted to reset their time. Else,
they break out of the second while loop and proceeds.

<br>

```python
    time_set_string = time_set.strftime("%B %d %Y %H:%M:%S")
    print(f"You have set your alarm at {time_set_string}")

    alarm_countdown(time_set)
```
Reminds the user their set datetime.

Goes into the 'alarm_countdown(time_set)' function, see Self-defined functions.

```python
    input("Enter any input to stop sound: ")
    winsound.PlaySound(None, 0)
```
Once alarm is ringing, this code allows user to stop the alarm with any input they add in.

<br>

<br>

## Output
```
Welcome to Simple Alarm Clock! (24hour, no GUI)
Current date and time: February 18 2023 17:05:29

Please select the date you would like the alarm to go off:
Year: 2023
Month: 2
Day: 18
Please select the time you would like the alarm to go off (up to 24hours):
Hour: 17
Min: 05
Sec: 40
Please select the time you would like the alarm to go off (up to 24hours):
Hour: 17
Min: 05
Sec: 59
You have set your alarm at February 18 2023 17:05:59
2023-02-18 17:05:50, 2023-02-18 17:05:59
2023-02-18 17:05:51, 2023-02-18 17:05:59
2023-02-18 17:05:52, 2023-02-18 17:05:59
2023-02-18 17:05:53, 2023-02-18 17:05:59
2023-02-18 17:05:54, 2023-02-18 17:05:59
2023-02-18 17:05:55, 2023-02-18 17:05:59
2023-02-18 17:05:56, 2023-02-18 17:05:59
2023-02-18 17:05:57, 2023-02-18 17:05:59
2023-02-18 17:05:58, 2023-02-18 17:05:59
2023-02-18 17:05:59, 2023-02-18 17:05:59
Alarm ringing!!
Enter any input to stop sound: w
```
Intentionally typed in wrong time to show how code reacts to invalid time set. During alarm ringing, default sound will play. After input entered, sound will
stop playing.

<br>

<br>

## Thoughts after the project
This project helped me to expand my knowledge on other Python libraries (datetime, time, winsound), and showed me new path to learn programming: 
Through the learning of libraries.

I believe that nowadays more frequently used libraries in the workplace in machine learning and data analysis are NumPy, Pandas, PyTorch, Matplotlib, etc. 

May start moving in that direction to make my Python knowledge into a professional skillset in the real world.

<br>

To be improved:
* Havent managed to test if this code works on months such as Feburary (29 days) or months with fewer that 31 days e.g. if user sets 31st February. Likely this code will
not work. Maybe can set a condition to ask for user input again for these dates that does not exist.
* Generally seems alright, but it seems quite tedious for user to put in so many parameters (year, month, day, hour, minutes, second)

<br>

Have a gif:

![Semantic description of image](https://media.tenor.com/BjEiyboaimYAAAAS/cat-cool-cat.gif)
