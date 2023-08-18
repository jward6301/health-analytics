# health-analytics
This is an assignment from HHA 506 as a primer for the Fall HHA 504 &amp; 507 classes.


## Summary of Variables
The number variables are ages and weights for both patients. 
The string variable is the patient's names.
The list is the Chief complaints.
The dictionary is past medical history that includes chief complaints, medical conditions, curent medications and past medications

## Explanation of the functions
I created two functions, one focusing on blood sugar and the other on BPM. Each function's outcome is dependent on two variables. For the blood sugar function, it is dependent on the blood sugar level and medical conditions, under past medical history. If the blood sugar is above 100 and the medical conditions states a history of hyperglycemia, it will return monitor patient and provide insulin. If neither conditions are met or only one is met, it will return patient is okay to go home. for the BPM function, it is dependent on the BPM and medical conditions, under past medical history. If the BPM is above 120 and the medical conditions states a history of hypertension, it will return monitor patient and provide beta-blockers. If neither conditions are met or only one is met, it will return patient is okay to go home.

## Expected output based on example data
The expected output is based off of the BPM function for both patients. For Pateint A, Frances, the expected output is monitor patient and provide beta-blockers. For Patient B, Hope, the expected outcome is patient is okay to go home. The output will also mention who each pateint is and what their BPM result is. 