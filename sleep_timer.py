import os
import time


# Ask how long until PC should shutdown in minutes and store as 'shutdown_in_hours'.
shutdown_in_hours = input("How many hours until PC shutdown?: ")

print(f'You have chosen ' + str(shutdown_in_hours) + ' hours.')

time.sleep(2)

# Multiply shutdown_in_hours by 3600 to create 'shutdown_in_seconds'.
shutdown_in_seconds = int(float(shutdown_in_hours) * 3600)

print(f'Command executed = shutdown -s -t ' + str(shutdown_in_seconds))

# Input command to shutdown PC after desired amount.
os.system(f'cmd /c "shutdown -s -t {shutdown_in_seconds}"')


time.sleep(2)