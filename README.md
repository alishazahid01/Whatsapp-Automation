WhatsApp Automation Documentation
Introduction

The "WhatsApp Automation" script is a Python script that automates sending greetings messages on WhatsApp using the pywhatkit library. It determines the time of the day and sends an appropriate greeting message based on the time. This documentation provides an overview of the code structure, usage, and functionality of the WhatsApp Automation script.
Getting Started

To use the WhatsApp Automation script, follow these steps:

    Install the required Python libraries by running the following command:

    bash

pip install pywhatkit

Clone or download this repository to your local machine.

Open the Python script in your preferred code editor or integrated development environment (IDE).

Execute the script using the following command:


    python whatsapp_automation.py

    Follow the prompts to enter the WhatsApp contact number you want to send greetings to.

Code Structure

The WhatsApp Automation script consists of the following components:
1. send_greetings Function

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

This function is responsible for sending greetings messages on WhatsApp. It determines the current time and selects an appropriate greeting message based on the time of the day. It then uses the pywhatkit.sendwhatmsg function to send the message to the specified WhatsApp contact. The wait_time parameter is set to 15 seconds to allow time for WhatsApp Web to open.
2. Main Execution Block

if __name__ == "__main__":
    contact = input("Enter the contact number: ")
    send_greetings(contact)

The main execution block of the script prompts the user to enter the WhatsApp contact number to which the greetings message should be sent. It then calls the send_greetings function to initiate the automation process.
Usage

    Run the Python script as described in the "Getting Started" section.

    Enter the WhatsApp contact number (with the country code) you want to send greetings to when prompted.

    The script will determine the time of the day and select an appropriate greeting message (e.g., "Good Morning," "Good Afternoon," "Good Evening," or "Good Night").

    It will then use pywhatkit to send the greeting message to the specified contact on WhatsApp Web.

    The script will print a confirmation message indicating that the message has been sent.

    Review the WhatsApp Web application to see the sent message.

Conclusion

The "WhatsApp Automation" script allows you to automate sending greetings messages on WhatsApp based on the time of the day. It simplifies the process of sending routine messages and can be customized to send different messages for various times of the day. This tool can be useful for sending automated reminders, greetings, or notifications on WhatsApp.
