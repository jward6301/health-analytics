import pandas as pd
import numpy as np

# These are the pateints

PatientA = {
    "fullname": "Frances Doe",
    "Age": 23,
    "Sex": "F",
    "Weight": 145,
    "ChiefComplaint": "headaches",
    "BPM": 135,
    "Bloodsugar": 75,
    "PastMedicalHistory": {
        "MedicalConditions": ["hypertension", "allergies", "acute eczema"],
        "CurrentMedications": ["flonase"],
        "PastMedications": ["claritin", "corticosteroids"]
    }
}
PatientB = {
    "fullname": "Hope Smith",
    "Age": 42,
    "Sex": "F",
    "Weight": 175,
    "ChiefComplaint": "tiredness",
    "BPM": 94,
    "Bloodsugar": 210,
    "PastMedicalHistory": {
        "MedicalConditions": ["hyperglycemia", "sleep apnea", "allergies"],
        "CurrentMedications": ["insulin", "claritin"],
        "PastMedications": ["modafinil"]
    }
}

#functions

def Bloodsugar_concern(BPM, Bloodsugar, MedicalConditions):
    if Bloodsugar > 100 and "hyperglycemia" in MedicalConditions:
        return "monitor patient and provide insulin"
    else:
        return "patient is okay to go home"

def BPM_concern(BPM, Bloodsugar, MedicalConditions):
    if BPM > 120 and "hypertension" in MedicalConditions:
        return "monitor patient and provide beta-blockers"
    else:
        return "patient is okay to go home"

#print

for key, value in PatientA.items():
    if key == "fullname":
        print("Patient A:", value)        

for key, value in PatientB.items():
    if key == "fullname":
        print("Patient B:", value)


#example run

BPM_result = BPM_concern(PatientA["BPM"], PatientA["Bloodsugar"], PatientA["PastMedicalHistory"]["MedicalConditions"])
print("patient name:", PatientA["fullname"], "BPM_result:", BPM_result)

BPM_result = BPM_concern(PatientB["BPM"], PatientB["Bloodsugar"], PatientB["PastMedicalHistory"]["MedicalConditions"])
print("patient name:", PatientB["fullname"], "BPM_result:", BPM_result)

