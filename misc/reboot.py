# pretty simple py script that will reboot linux machine


# This script imports the 'os' module and uses the 'system()' function to run the command sudo reboot in the terminal

import os
ask = input("Are you sure you want to reboot the machine (yes/no)? ")
if ask == 'yes':
    os.system("sudo reboot")
else:
  print("Reboot cancelled.")
# This will be using sudo command in script may prompt for password. And also, make sure you have the correct permissions to run the command.




# Using Subprocess method. 

# import subprocess
# # confirmation before rebooting the machine using input function
# confirm = input("Are you sure you want to reboot the machine (yes/no)? ")
# if confirm ==  'yes':
#     subprocess.run(["sudo", "reboot"])
# else:
#     print("Reboot cancelled")