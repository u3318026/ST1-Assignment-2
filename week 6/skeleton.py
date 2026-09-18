# Define a class to represent the possible status states of an appointment
class AppointmentStatus:
    # Set the initial booking state string
    BOOKED = "Booked"
    # Set the confirmed state string
    CONFIRMED = "Confirmed"
    # Set the cancelled state string
    CANCELLED = "Cancelled"
    # Set the completed state string
    COMPLETED = "Completed"
    # Set the no-show state string
    NO_SHOW = "No-show"


# Define a class to store and manage patient information
class Patient:
    # Initialize a new Patient object with its required attributes
    def __init__(self, patient_id, name, date_of_birth, contact_details):
        # Assign the unique patient ID
        self.patient_id = patient_id
        # Assign the patient's full name
        self.name = name
        # Assign the patient's date of birth
        self.date_of_birth = date_of_birth
        # Assign the patient's contact details
        self.contact_details = contact_details

    # Method to allow a patient to request a new appointment
    def request_appointment(self):
        pass

    # Method to allow a patient to view their past appointments
    def view_appointment_history(self):
        pass


# Define a class to store and manage practitioner (GP) information
class Practitioner:
    # Initialize a new Practitioner object with its required attributes
    def __init__(self, practitioner_id, name):
        # Assign the unique practitioner ID
        self.practitioner_id = practitioner_id
        # Assign the practitioner's full name
        self.name = name
        # Initialize an empty list to store available time slots
        self.availability = []

    # Method to check if the practitioner is free at a given date/time
    def is_available(self, date_time):
        # Placeholder for checking availability logic
        pass

    # Method to accept and confirm an appointment request
    def confirm_appointment(self):
        # Placeholder for confirmation logic
        pass


# Define a class to link patients and practitioners for consultations
class Appointment:
    # Initialize a new Appointment linking a patient and a practitioner
    def __init__(self, appointment_id, date_time, patient, practitioner):
        # Assign the unique appointment ID
        self.appointment_id = appointment_id
        # Assign the scheduled date and time    
        self.date_time = date_time
        # Store a reference to the associated Patient object
        self.patient = patient
        # Store a reference to the associated Practitioner object
        self.practitioner = practitioner
        # Set the default initial status to 'Booked'    
        self.status = AppointmentStatus.BOOKED

    # Method to finalize and validate the booking process
    def book(self):
        # Placeholder for booking logic
        pass

    # Method to cancel the appointment while preserving history
    def cancel(self):
        # Placeholder for cancellation logic
        pass

    # Method to mark the appointment as completed after consultation
    def complete(self):
        # Placeholder for completion logic
        pass