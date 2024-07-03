from Doctor import Doctor
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
class Address:
    def __init__(self, street, city, state, postcode):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__postcode = postcode

    def get_full_address(self):
        return f'{self.__street}, {self.__city}, {self.__state} {self.__postcode}'

    def get_postcode(self):
        """Get the postcode from the address."""
        return self.__postcode



class Appointment:
    def __init__(self, month, patient, doctor):
        lowercase_month = month.lower()
        if lowercase_month not in (m.lower() for m in MONTHS):
            raise ValueError("Invalid month. Please choose from the fixed list of months.")
        self.__month = lowercase_month
        self.__patient = patient
        self.__doctor = doctor

    def get_month(self):
        return self.__month

    def get_patient(self):
        return self.__patient

    def get_doctor(self):
        return self.__doctor



class Patient:
    def __init__(self, first_name, surname, age, mobile, address):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__address = address
        self.__doctor = None
        self.__symptoms = []
        self.__appointments = []
        self.__illness_type = None  

    

    def get_illness_type(self):
        return self.__illness_type

    def set_illness_type(self, illness_type):
        self.__illness_type = illness_type

   

    def add_appointment(self, appointment):
        """Add an appointment to the patient."""
        self.__appointments.append(appointment)

    def get_appointments(self):
        """Get the list of appointments."""
        return self.__appointments

   
    def set_doctor(self, doctor):
        self.__doctor = doctor

    
    def link_doctor(self, doctor):
        """Link a doctor to the patient."""
        self.__doctor = doctor

   

    def get_doctor(self):
    
        if isinstance(self.__doctor, Doctor):
            return self.__doctor.full_name()
        elif isinstance(self.__doctor, str):
            return self.__doctor
        else:
            return 'Not assigned'


    def get_patient_details(self):
         details = {
            'Name': f'{self.__first_name} {self.__surname}',
            'Age': self.__age,
            'Mobile': self.__mobile,
            'Address': str(self.__address),
            'Doctor': self.__doctor.full_name() if isinstance(self.__doctor, Doctor) else 'None',
            'Symptoms': self.__symptoms,
            'Postcode': self.__address.get_postcode(),
        }
         return details


    def full_name(self):
        """Get the full name of the patient."""
        return f'{self.__first_name} {self.__surname}'

    def get_full_name(self):
        """Get the full name of the patient."""
        return f'{self.__first_name} {self.__surname}'

   

    def add_symptom(self, symptom):
        """Add a symptom to the patient."""
        self.__symptoms.append(symptom)
    
    def print_symptoms(self):
        """Print the patient's symptoms."""
        print(f"Symptoms: {', '.join(self.__symptoms)}")

    def view_symptoms(self):
        """View all recorded symptoms."""
        if not self.__symptoms:
            print('No symptoms recorded.')
        else:
            print('Symptoms:')
            for symptom in self.__symptoms:
                print(f'- {symptom}')

    def get_symptoms(self):
        """Get the list of symptoms."""
        return self.__symptoms

    def __str__(self):
        doctor_info = self.__doctor.full_name() if isinstance(self.__doctor, Doctor) else self.__doctor
        return f'{self.full_name():^30}|{doctor_info:^30}|{self.__age:^3}|{self.__mobile:^15}|{self.__address.get_full_address():^10}'


    def get_first_name(self):
        return self.__first_name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_mobile(self):
        """Get the mobile number of the patient."""
        return self.__mobile

    def get_address(self):
        """Get the address of the patient."""
        return self.__address

    def get_postcode(self):
        """Get the postcode of the patient."""
        return self.__address.get_postcode() if self.__address else 'Not available'
    
    
    
    



