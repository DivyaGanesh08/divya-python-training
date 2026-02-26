
class Patient():
    def calculate_bill(self):
        pass
class InPatient(Patient):
    def calculate_bill(self):
        return 20000

patient_type = input("Enter Patient Type (InPatient): ")

if patient_type.lower() == "inpatient":
    patient = InPatient()
else:
    print("Invalid Patient Type")
    exit()

print("Total Bill:", patient.calculate_bill())