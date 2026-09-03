For the AI usage I asked it:

"Act as a Python tutor.
I am learning introductory software technology.
Here is a small appointment-booking function.
1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.


print("Welcome to Smart Care!")
#first appointment
patient_name: str = input("Please enter your name: ")
practitioner_name: str = input(f"Hello, {patient_name}! Please enter the practitioner's name: ")
appointment_date_time= input("Please enter the appointment date and time: ")


#second appointment
patient_name2: str = input("Please enter your name: ")
practitioner_name2: str = input(f"Hello, {patient_name2}! Please enter the practitioner's name: ")
appointment_date_time2= input("Please enter the appointment date and time: ")

if practitioner_name == practitioner_name2 and appointment_date_time == appointment_date_time2:
    print("Warning: You have scheduled two appointments with the same practitioner at the same time.")
    raise ValueError("You cannot schedule two appointments with the same practitioner at the same time.")
else:
    print(f"Appointment 1: {patient_name} with {practitioner_name} on {appointment_date_time}")
    print(f"Appointment 2: {patient_name2} with {practitioner_name2} on {appointment_date_time2}")"


This is based upon my code and the requiremtn from the lab document:
It gave me this to answer as the 2 questions 

"📝Two questions to test your understanding
Why might using a list of dictionaries be better than using separate variables like patient_name2?

What is the purpose of raising a ValueError in this program?

If you want, we can walk through how to implement one of the improvements — just pick one."

I answered the 2 questions saying: It is better to use a list dictionary since it lets me store as many apointments under 1 variable as I want

For the second one I said I raise the value error since it is important to flag conflicting appointments.




I then asked it to perform this (copy paste from the lab document) "Ask AI to create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Explicitly prohibit a database or GUI."

It produced:

def create_appointment():
    patient = input("Enter patient name: ")
    practitioner = input(f"Hello {patient}, enter practitioner name: ")
    time = input("Enter appointment date and time: ")

    appointment = {
        "patient": patient,
        "practitioner": practitioner,
        "time": time
    }

    print("Appointment saved!")
    return appointment
create_appointment()