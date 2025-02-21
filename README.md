# password-checker
Password strength checker completed as part of an assignment for Computer Ethics at the University of Utah


This program takes a password as input and evaluates the strength of it, printing feedback to the terminal as output.

To run this program, download passChecker.py and run python on it.  This might be as simple as typing `Python3 <path-to-file>` into a command prompt, but it varies based on your computer.

This tool is for educational purposes only.  Please do not type your real passwords in here.  This program processes them as plain text strings, with no attempt to hide them.

That aside, it also isn't a very practical evaluation of a password.  The evaluation is too simple: passwords fulfilling more of the below conditions are stronger:
* Length at least 8 characters
* Length at least 12 characters
* Contains an upper case letter
* Contains a lower case letter
* Contains a numerical digit
* Contains a special character
