import platform
import subprocess
from w10_master_list import cell_path_master_list as ml

successful = []

failed = []

for pc in ml:
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    host = pc["asset_num"]

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        print("Success")
        successful.append(pc)
        
    else:
        print("Failed")
        failed.append(pc)

print("Successful pings:")
print(successful)
print("\nFailed pings:")
print(failed)

success_textfile = open("successful.txt", "w")
for element in successful:
    success_textfile.write(element + "\n")
success_textfile.close

fail_textfile = open("failed.txt", "w")
for element in failed:
    fail_textfile.write(element + "\n")
fail_textfile.close
