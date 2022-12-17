# importing the subprocess module
import subprocess
import os
# store the profiles' data in a variable called data
# running the first command using the subprocess.check_output

# subprocess.check_output(["ls"])
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# store the profile by converting it into alist
profiles = [i.split(':')[1][1:-1] for i in data if 'All User Profile' in i]

# using a loop in checking and printing any wifi password
# if they are available, use the second command
for i in profiles:
    # running the  second command to check the passwords
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key = clear']).decode('utf-8').split(
        '\n')
    # storig the passwors after converting them to a myList
    results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]

    # printing the profile passwors using their WIFI name and passwords
    try:
        print('{:<30|{:<}'.format(i,results[0]))
    except IndexError:
        print('{<30|{:<}'.format(i,''))
