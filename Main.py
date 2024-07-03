import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
from Admin import Admin
from Doctor import Doctor
from Patient import Patient, Address

def main():
    """
    The main function to be run when the program executes.
    """

    # Initializing the actors
    admin = Admin('admin', '123', Address('B1 1AB', 'Cityville', 'State', '12345'))
    doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'),
               Doctor('Jone', 'Carlos', 'Cardiology')]
    patients = admin.load_patients_from_file()
    admin.set_patients(patients)
    discharged_patients = []

    # Keep trying to log in until the login details are correct
    while True:
        if admin.login():
            running = True  # Allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # Print the menu
        print('Choose the operation:')
        print(' 1- Manage Doctors')
        print(' 2- Manage Patients ')
        print(' 3- Assign doctor to a patient')
        print(' 4- Update Admin Details') 
        print(' 5- Relocate patient') 
        print(' 6- Give Patient Appointment')
        print(' 7- View Report')
        print(' 8- Quit')

        # Get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)

        elif op == '2':
            # 2- Manage Patients sub-menu
            print('Choose the operation for managing patients:')
            print(' a- View Patients')
            print(' b- Discharge Patients')
            print(' c- View Discharged Patients')
            print(' d- Add Symptoms to Patient')
            sub_op = input('Sub-option: ')

            if sub_op == 'a':
                # View Patients
                admin.view_patient(patients)

                # Ask if the user wants to view patient symptoms
                show_symptoms = input('Do you want to view patient symptoms? (yes/no): ').lower()

                if show_symptoms == 'yes':
                    # Ask for the ID of the patient to view symptoms
                    try:
                        patient_id = int(input('Enter the ID of the patient to view symptoms: '))
                        selected_patient = patients[patient_id - 1]  # Adjust index for 1-based user input

                        # View symptoms for the selected patient
                        admin.view_patient_symptoms(selected_patient)

                    except (ValueError, IndexError):
                        print('Invalid input. Please enter a valid ID.')

            elif sub_op == 'b':
                # Discharge Patients
                admin.view_patient(patients)

                while True:
                    op = input('Do you want to discharge a patient (Y/N):').lower()

                    if op == 'yes' or op == 'y':
                        admin.discharge(patients, discharged_patients)
                        print('Patient discharged.')
                        break

                    elif op == 'no' or op == 'n':
                        break

                    # Unexpected entry
                    else:
                        print('Please answer by yes or no.')

            elif sub_op == 'c':
                # View Discharged Patients
                admin.view_discharge(discharged_patients)

            elif sub_op == 'd':
                # Add Symptoms to Patient
                admin.add_symptoms_to_patient(patients)

            else:
                print('Invalid sub-option. Try again.')

        elif op == '3':
            # 3- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '4':
            # 4- Update Admin Details
            admin.update_details()

        elif op == '5':
            admin.relocate_patient_to_doctor(patients, doctors)
            
        
        elif op == '6':
            admin.give_patient_appointment(patients, doctors)

        elif op == '7':
            # 7- Request Management Report
            admin.request_management_report(doctors, patients)

        elif op == '8':
            # 5- Quit
            print('Exiting the program. Goodbye!')
            running = False

        else:
            # The user did not enter an option that exists in the menu
            print('Invalid option. Try again')


if __name__ == '__main__':
    main()
