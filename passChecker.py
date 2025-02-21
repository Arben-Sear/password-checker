'''
passChecker
Garrett Brothers
Ethics in Computing
Feb 20, 2025
Professor Brown
The University of Utah

This program prompts the user to enter a password so it can be evaluated.  The evaluation is simple: passwords fulfilling more of the below conditions are stronger:
* Length at least 8 characters
* Length at least 12 characters
* Contains an upper case letter
* Contains a lower case letter
* Contains a numerical digit
* Contains a special character

See https://github.com/Arben-Sear/password-checker/ for more details, including important warnings.
'''


'''
Main
'''

print("Welcome.  Please input a password to evaluate its strength.")
password = input()
strength = 0

if any(c for c in password if c.islower()): strength += 1 # credit https://stackoverflow.com/questions/12934997/how-to-detect-lowercase-letters-in-python
if any(c for c in password if c.isupper()): strength += 1
if any(c for c in password if c.isdigit()): strength += 1
if any(c for c in password if not c.isupper() and not c.islower() and not c.isdigit()): strength += 1
if len(password) >= 8: strength += 1
if len(password) >= 12: strength += 1

# A password can have strength up to 6
if strength == 6: print("Excellent password!")
elif strength == 5: print("Very strong password!")
elif strength == 4: print("Strong password!")
elif strength == 3: print("Moderate password!")
elif strength == 2: print("Okay password!")
elif strength == 1: print("Weak password!")
else: print("Password was very weak (contains no characters?)")