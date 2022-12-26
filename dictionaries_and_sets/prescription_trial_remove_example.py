"""
In this program we will see how to use remove() to remove items from the set and why using remove() here is a better option than using discard()

"""

from priscription_data import *

# Taking some of the patients as an example. We will check the medications of these patients.
#trial_patients= ["Denise", "Eddie", "Frank", "Goergia","Kenny"] # This will fail with remove() that is what we want. This happens because Kenny is included in the group by mistake.
# One solution is to check if we are only considering the aptients that take the wafarin. This is done by cheking if the wafarin is a part of the set prescription.

trial_patients= ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]


for patient in trial_patients:
    prescription= patients[patient] # This will give the mediacation prescribed to each of the above patient. 
    print(prescription, patients)
    if warfarin in prescription:
        # We need to remove waferin and replace it with edoxaban
        prescription.remove(warfarin) #Here remove is important. Because if we do not have wafarin for the patient, it will not affect the output. For example Kenny. 
        prescription.add(edoxaban)

    else:
        print(f"{patient} does not have wafarin in prescription. This is a mistake. Fix it.")
    


