from Doctor import Doctor
import json
from Patient import Patient
from Patient import Address
from Patient import Appointment
from collections import defaultdict
from collections import Counter 
from datetime import datetime
import matplotlib.pyplot as plt
from Doctor import Doctor  

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
class Admin:
    
    MONTHS = MONTHS
   
    
    

    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address=''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index + 1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Returns:
            bool: True if login is successful, False otherwise
        """
        print("-----Login-----")

        
        while True:
            # Get the details of the admin
            username_input = input('Enter the username: ')
            password_input = input('Enter the password: ')

            
            if username_input == self.__username and password_input == self.__password:
                return True  # Successful login
            else:
                print('Incorrect username or password. Please try again.')


    def find_index(self, index, doctors):
        
        if index in range(0, len(doctors)):
            return True
        else:
            return False
        
    def set_patients(self, patients):
        self.patients = patients

    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname, and ...
                            ... the specialty of the doctor in that order.
        """
        first_name = input("Enter doctor's first name: ")
        surname = input("Enter doctor's surname: ")
        specialty = input("Enter doctor's specialty: ")

        return first_name, surname, specialty
   


    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register doctor')
        print(' 2 - View doctor')
        print(' 3 - Update doctor ')
        print(' 4 - Delete doctor')

        op = input('Input: ')  # Take user input for operation

        # Register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, specialty = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break  # save time and end the loop

            if not name_exists:
                new_doctor = Doctor(first_name, surname, specialty)
                doctors.append(new_doctor)
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index:
                        break
                    else:
                        print("Doctor not found")

                except ValueError:  
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            update_option = int(input('Input: '))

            if update_option == 1:
                new_first_name = input('Enter the new first name: ')
                doctors[index].set_first_name(new_first_name)
            elif update_option == 2:
                new_surname = input('Enter the new surname: ')
                doctors[index].set_surname(new_surname)
            elif update_option == 3:
                new_specialty = input('Enter the new specialty: ')
                doctors[index].set_speciality(new_specialty)
            else:
                print('Invalid option.')

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) - 1
                if self.find_index(doctor_index, doctors):
                    del doctors[doctor_index]
                    print('Doctor deleted.')
                else:
                    print('The id entered is incorrect')
            except ValueError:
                print('Invalid input. Please enter a valid ID.')

        # if the id is not in the list of patients
        else:
            print('Invalid operation chosen. Check your spelling!')
    def view_patient(self, patients):
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        
        # Sort patients by surname
        sorted_patients = sorted(patients, key=lambda patient: patient.get_surname())

        for index, patient in enumerate(sorted_patients):
            doctor_info = patient.get_doctor()
            mobile = patient.get_mobile()
            address = patient.get_address()
            print(f'{index + 1:3}| {patient.get_full_name():30}| {doctor_info:30}| {patient.get_age():3}| {mobile:^15}| {patient.get_postcode()}')


    def add_symptoms_to_patient(self, patients):
        print("-----Add Symptoms to Patient-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        try:
            patient_index = int(input('Enter the ID of the patient to add symptoms: ')) - 1
            if 0 <= patient_index < len(patients):
                symptoms = input('Enter symptoms (comma-separated): ').split(',')
                illness_type = input('Enter illness type: ')  # Prompt for illness type
                for symptom in symptoms:
                    patients[patient_index].add_symptom(symptom)
                patients[patient_index].set_illness_type(illness_type)  # Set the illness type
                print('Symptoms and illness type added to the patient.')
            else:
                print('Invalid patient ID.')
        except ValueError:
            print('Invalid input. Please enter a valid ID.')


         
    def view_patient_symptoms(self, patient):
    
        patient.view_symptoms()


    def assign_doctor_to_patient(self, patients, doctors):
        """
       Allow the admin to assign a doctor to a patient
       Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')
 
        try:
        # patient_index is the patient ID minus one (-1)
           patient_index = int(patient_index) - 1
   
        # check if the id is not in the list of patients
           if patient_index not in range(len(patients)):
              print('The id entered was not found.')
              return  

        except ValueError:  # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return  # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()  # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
        # doctor_index is the doctor ID minus one (-1)
           doctor_index = int(doctor_index) - 1

        # check if the id is in the list of doctors
           if self.find_index(doctor_index, doctors) is not False:
            # link the patients to the doctor and vice versa
              selected_doctor = doctors[doctor_index]
              patients[patient_index].set_doctor(selected_doctor)

            # Add the patient to the list of patients the doctor is handling
              selected_doctor.add_patient(patients[patient_index])

              print('The patient is now assigned to the doctor.')

        # if the id is not in the list of doctors
           else:
                print('The doctor ID entered was not found.')

        except ValueError:  
              print('The doctor ID entered is incorrect')




    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1

            if self.find_index(patient_index, patients):
                discharged_patient = patients.pop(patient_index)
                discharge_patients.append(discharged_patient)
                print('Patient discharged.')
            else:
                print('The id entered is incorrect.')
        except ValueError:
            print('Invalid input. Please enter a valid ID.')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')

        for index, discharged_patient in enumerate(discharged_patients):
            print(f'{index + 1:3}| {discharged_patient.get_full_name():30}| {discharged_patient.get_doctor():30}| {discharged_patient.get_age():3}| {discharged_patient.get_mobile():15}| {discharged_patient.get_postcode()}')

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            new_username = input('Enter the new username: ')
            
            self.__username = new_username
            print('Username updated.')

        elif op == 2:
            new_password = input('Enter the new password: ')
            # validate the password
            if new_password == input('Enter the new password again: '):
                self.__password = new_password
                print('Password updated.')
            else:
                print('Passwords do not match. Update failed.')

        elif op == 3:
            new_address = input('Enter the new address: ')
            
            self.__address = new_address
            print('Address updated.')

        else:
            print('Invalid option.')
    def save_patients_to_file(self, patients, file_path='patients.json'):
        """
        Save the patients' data to a file in JSON format.
        Args:
            patients (list): List of patient objects.
            file_path (str): Path to the file. Defaults to 'patients.json'.
        """
        patients_data = [patient.get_patient_details() for patient in patients]

        with open(file_path, 'w') as file:
            json.dump(patients_data, file, indent=2)
        print(f'Patients data saved to {file_path}.')

    def load_patients_from_file(self):
        """
        Load patients' data from a file in JSON format.
        Returns:
            list: List of Patient objects loaded from the file.
        """
        try:
            with open('patients.json', 'r') as file:
                patients_data = json.load(file)

            patients = []
            for data in patients_data:
                
                name = data.get("Name")
                age = data.get("Age")
                mobile = data.get("Mobile")
                address_data = data.get("Address")
                doctor = data.get("Doctor")
                symptoms = data.get("Symptoms", [])

                
                if len(address_data) < 4:
                    address_data += ['']

                
                address = Address(*address_data.split(', '))
                patient = Patient(*name.split(), age, mobile, address) 
                patient.link_doctor(doctor)  
                for symptom in symptoms:
                    patient.add_symptom(symptom)  

                patients.append(patient)

            return patients

        except FileNotFoundError:
            print("Patients file not found.")
            return []
    def relocate_patient_to_doctor(self, patients, doctors):
        print("-----Relocate Patient to Another Doctor-----")
        print('ID |          Full Name           |      Doctor`s Full Name      ')

        # Display a list of patients with their IDs and assigned doctors
        for index, patient in enumerate(patients):
            print(f'{index + 1:3}| {patient.get_full_name():30}| {patient.get_doctor():30}')

        try:
            # Get the ID of the patient to relocate
            patient_index = int(input('Enter the ID of the patient to relocate: ')) - 1

            # Check if the patient index is valid
            if self.find_index(patient_index, patients):
                # Display a list of doctors to choose from
                print('Select the new doctor for the patient:')
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)

                try:
                    # Get the ID of the new doctor
                    new_doctor_index = int(input('Enter the ID of the new doctor: ')) - 1

                    # Check if the new doctor index is valid
                    if self.find_index(new_doctor_index, doctors):
                        # Relocate the patient to the new doctor
                        patients[patient_index].set_doctor(doctors[new_doctor_index])
                        print('Patient relocated successfully.')
                    else:
                        print('Invalid new doctor ID.')

                except ValueError:
                    print('Invalid input. Please enter a valid ID for the new doctor.')

            else:
                print('Invalid patient ID.')

        except ValueError:
            print('Invalid input. Please enter a valid ID for the patient.')




    def request_management_report(self, doctors, patients):
        print("----- Management Report -----")

        # Total number of doctors in the system
        print(f"Total number of doctors in the system: {len(doctors)}")

        # Total number of patients per doctor
        print("\nTotal number of patients per doctor:")
        for doctor in doctors:
            patient_count = len(doctor.get_patients())
            print(f"{doctor.full_name()}: {patient_count}")

        # Total number of appointments per month per doctor
        appointments_per_month_per_doctor = self.get_appointments_per_month_per_doctor(patients)

        print("\nTotal number of appointments per month per doctor:")
        print('Doctor Name |', ' | '.join(self.MONTHS)) 
  
        for doctor_name, monthly_appointments in appointments_per_month_per_doctor.items():
            print(doctor_name, end=' | ')
            for month in self.MONTHS:
                appointments_count = monthly_appointments.get(month, 0)
                print(f'{appointments_count:^2}', end=' | ')
            print() 

        # Total number of patients based on the illness type
        illness_types_count = defaultdict(int)
        for patient in patients:
            for symptom in patient.get_symptoms():
                illness_types_count[symptom] += 1

        if not illness_types_count:
          print("No illness type recorded. You can give patients an illness type under 'manage patients'.")
        else:
    
          print("\nTotal number of patients based on the illness type:")
          for illness_type, count in illness_types_count.items():
              print(f"{illness_type}: {count}")

        show_visual_report = input('Do you want to see the visual report? (yes/no): ').lower()

        if show_visual_report == 'yes':
            print('Select the type of visual report:')
            print(' 1 - Total number of doctors')
            print(' 2 - Total number of patients per doctor')
            print(' 3 - Total Number of Appointments per Month per Doctor')
            print(' 4 - Total Number of Patients Based on Illness Type')  

            visual_report_option = input('Option: ')

            if visual_report_option == '1':
                self.plot_total_doctors(doctors)
            elif visual_report_option == '2':
                self.plot_patients_per_doctor(doctors)
            elif visual_report_option == '3':
                self.plot_appointments_per_month_per_doctor(doctors, patients)
            elif visual_report_option == '4':  # New condition
                self.plot_patients_by_illness_type(patients)
            
            else:
                print('Invalid visual report option.')

                





    def get_appointments_per_month_per_doctor(self, patients):
        """
        Get a report of the total number of appointments per month per doctor.

        Args:
            patients (list): List of Patient objects.

        Returns:
            dict: A nested dictionary with doctor names as keys and a dictionary
                  with months as keys and the corresponding total appointments as values.
        """
        appointments_report = defaultdict(lambda: defaultdict(int))

        for patient in patients:
            doctor = patient.get_doctor()
            if doctor and isinstance(doctor, Doctor):  
                doctor_name = doctor.full_name()
                for appointment in patient.get_appointments():
                    month = appointment.get_month()
                    appointments_report[doctor_name][month] += 1

        return appointments_report


  
              
    


    def plot_total_doctors(self, doctors):
        """
        Plot a bar chart showing the total number of doctors.
        Args:
            doctors (list<Doctor>): List of Doctor objects.
        """
        total_doctors = len(doctors)
        threshold_value = 10

        # Determine the color based on the threshold
        color = 'green' if total_doctors >= threshold_value else 'red'

        plt.bar(['Total Doctors'], [total_doctors], color=color)
        plt.axhline(y=threshold_value, color='r', linestyle='--', label='Threshold Value')

        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.title('Total Number of Doctors in the System')
        plt.legend()
        plt.show()


    def plot_patients_per_doctor(self, doctors):
        """
        Plot a bar chart of the total number of patients per doctor.
        Args:
            doctors (list<Doctor>): List of Doctor objects.
        """
        # Create lists to store doctor names and patient counts
        doctor_names = [doctor.full_name() for doctor in doctors]
        patient_counts = [len(doctor.get_patients()) for doctor in doctors]

        # Plotting bar chart
        plt.bar(doctor_names, patient_counts)
        plt.xlabel('Doctor')
        plt.ylabel('Total Number of Patients')
        plt.title('Total Number of Patients per Doctor')
        plt.show()
        
   




    def plot_appointments_per_month_per_doctor(self, doctors, patients):
        """
        Plot a bar chart showing the total number of appointments per month per doctor.
        Args:
            doctors (list<Doctor>): List of Doctor objects.
            patients (list<Patient>): List of Patient objects.
        """
        # Assuming each patient has a list of appointments, and each appointment has a month attribute
        doctor_names = [doctor.full_name() for doctor in doctors]
        months = [month.capitalize() for month in self.MONTHS]  # Ensure months are capitalized

        appointment_counts = {doctor.full_name(): {month: 0 for month in months} for doctor in doctors}

        for doctor in doctors:
            for patient in doctor.get_patients():
                for appointment in patient.get_appointments():
                    month_index = self.MONTHS.index(appointment.get_month().capitalize())
                    appointment_counts[doctor.full_name()][self.MONTHS[month_index]] += 1

        # Plotting bar chart
        for doctor_name in doctor_names:
            counts = [appointment_counts[doctor_name][month] for month in months]
            plt.bar(months, counts, label=doctor_name)

        plt.xlabel('Month')
        plt.ylabel('Total Number of Appointments')
        plt.title('Total Number of Appointments per Month per Doctor')
        plt.legend()
        plt.show()




    def give_patient_appointment(self, patients, doctors):
        print('Assign an appointment to a patient:')

        # Display doctors
        print('Available doctors:')
        for i, doctor in enumerate(doctors, 1):
            print(f'{i}. {doctor}')

        # Get the doctor's ID
        try:
            doctor_id = int(input('Enter the ID of the doctor: '))
            doctor = doctors[doctor_id - 1]  
        except (ValueError, IndexError):
            print('Invalid input. Please enter a valid ID.')
            return

        while True:
            # Display available months
            print('Available months:', ', '.join(MONTHS))

            # Get the appointment month
            month = input('Enter the month for the appointment: ')

            # Check if the entered month is valid
            if month.capitalize() in MONTHS:
                break
            else:
                print('Invalid month. Please enter a valid month.')

        # Display patients
        self.view_patient(patients)

        # Get the patient's ID
        try:
            patient_id = int(input('Enter the ID of the patient: '))
            patient = patients[patient_id - 1]  # Adjust index for 1-based user input
        except (ValueError, IndexError):
            print('Invalid input. Please enter a valid ID.')
            return

        # Create an Appointment object with patient and doctor information
        appointment = Appointment(month, patient, doctor)

        # Assign the doctor to the patient
        patient.link_doctor(doctor)

        # Add the appointment to the patient and update the doctor's appointments
        patient.add_appointment(appointment)
        doctor.add_appointment(appointment)

        print(f'Appointment scheduled for {patient.full_name()} with {doctor.full_name()} in {appointment.get_month()}.')
        

    def view_appointments_per_month_per_doctor(self, doctors, patients):
        """
        Print the total number of appointments per month per doctor.

        Args:
            doctors (list<Doctor>): List of Doctor objects.
            patients (list<Patient>): List of Patient objects.
        """
        appointments_report = self.get_appointments_per_month_per_doctor(patients)

        # Print the report
        print("-----Total Number of Appointments per Month per Doctor-----")
        print('Doctor Name |', ' | '.join(self.MONTHS))  # Header

        for doctor in doctors:
            doctor_name = doctor.full_name()
            appointments_count = [appointments_report[doctor_name][month] for month in self.MONTHS]
            print(f'{doctor_name:12} |', ' | '.join(map(str, appointments_count)))

    
    


    def plot_patients_by_illness_type(self, patients):
        illness_types_count = defaultdict(int)
        for patient in patients:
            for symptom in patient.get_symptoms():
                illness_types_count[symptom] += 1

        print("\nTotal number of patients based on the illness type:")
        for illness_type, count in illness_types_count.items():
            print(f"{illness_type}: {count}")

        # Plotting the bar graph
        labels, values = zip(*illness_types_count.items())
        plt.bar(labels, values)
        plt.xlabel('Illness Type')
        plt.ylabel('Number of Patients')
        plt.title('Total Number of Patients Based on Illness Type')
        plt.show()
