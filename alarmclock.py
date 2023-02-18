import datetime
import winsound
import time

global datetime_today
datetime_today = datetime.datetime.today()

global datetime_today_string
datetime_today_string = datetime_today.strftime("%B %d %Y %H:%M:%S")

global date_today
date_today = datetime.date.today()

print("Welcome to Simple Alarm Clock! (24hour, no GUI)")
print(f"Current date and time: {datetime_today_string}")
print("")
time.sleep(2)

def main(): 
    while True:
        try:
            print("Please select the date you would like the alarm to go off:")
            a = user_input_date_year()
            b = user_input_date_month()
            c = user_input_date_day()

            dt_alarmtest = datetime.date(a, b, c)

            date_diff = dt_alarmtest - date_today 
            
            tdelta = datetime.timedelta(days=0)

            if date_diff >= tdelta:
                break
        except:
            print("Please re-enter the date!")


    while True:
        try:
            print("Please select the time you would like the alarm to go off (24hr clock):")
            x = user_input_date_hours()
            y = user_input_date_mins()
            z = user_input_date_secs()

            time_set = datetime.datetime(a, b, c, x, y, z)

            dt_diff = time_set - datetime.datetime.today()

            if dt_diff >= tdelta:
                break
        except:
            print("Please re-enter the time!")

    time_set_string = time_set.strftime("%B %d %Y %H:%M:%S")
    print(f"You have set your alarm at {time_set_string}")

    alarm_countdown(time_set)

    input("Enter any input to stop sound: ")
    winsound.PlaySound(None, 0)



#Infinite loop, did not add sound, so a default sound will play
def alarm_countdown(n):
    while True:
        current_time = datetime.datetime.today().replace(microsecond=0)
        time.sleep(1)
        print(f"{current_time}, {n}")

        if n == current_time:
            print("Alarm ringing!!")
            winsound.PlaySound("defaultsound", winsound.SND_ASYNC + winsound.SND_LOOP)
            break

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
    return x

main()
    
