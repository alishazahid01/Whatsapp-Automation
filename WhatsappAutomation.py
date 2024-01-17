# Whatsapp Automation  
import pywhatkit
import datetime

def send_greetings(contact):
    current_time = datetime.datetime.now().time()

    if current_time < datetime.time(12):
        message = "Good Morning (This is an Automated Message)"
    elif current_time < datetime.time(17):
        message = "Good Afternoon (This is an Automated Message)"
    elif current_time < datetime.time(21):
        message = "Good Evening (This is an Automated Message)"
    else:
        message = "Good Night"

    pywhatkit.sendwhatmsg(contact, message, current_time.hour, current_time.minute + 1, wait_time=15)
    print(f"{message} message sent!")

if __name__ == "__main__":
    contact = input("Enter the contact number: ")
    send_greetings(contact)

# Credit : Alisha Zahid 
