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


print(create_appointment())