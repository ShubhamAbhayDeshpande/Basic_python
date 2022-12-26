"""
This code will demonstrate how can we use pop() method in the sets. 

Since we cannot index sets, pop() will genrally takeout a random elelment from the set. But, this is fine most of the times.

"""

from priscription_data import patients

trial_patients= {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

# while trial_patients:
#     patient= trial_patients.pop() # This line will take out a random patient from the set.
#     print(patient) # This line will print the name of that patient. 

# send the prescription of the patients to the farmacy. 
while trial_patients:
    patient= trial_patients.pop()# This line will take out a random patient from the set.
    patients_prescription= patients[patient]# This will take the prescription of that patient. 
    print(patient,':', patients_prescription)# This line will print the name of that patient and the contents of the prescription.