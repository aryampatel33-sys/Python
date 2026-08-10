medical_cause = input(" Do you have a medical cause? (Y/N) ") .strip().upper()
if medical_cause == 'Y':
    print("You're allowed to skip the exam")
else:
    attend = int(input("How much is your attendance:" ))
if attend >= 75:
     print("You're allowed to skip the exam")
else:
     print("You're not allowed to skip the exam")