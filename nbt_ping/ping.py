import platform
import subprocess
from datetime import date

today = date.today()

cell_path_pcs = {
    "online": [],
    "offline": [],
}

def myping():
    while True:
        parameter = '-n' if platform.system().lower()=='windows' else '-c'

        host = input("Please enter asset number:\n")

        command = ['ping', parameter, '1', host]
        response = subprocess.call(command)

        if response == 0:
            print("Ping successful")
            cell_path_pcs["online"].append(
                {
                    "asset_number": host,
                    "last_successful_ping": today.strftime("%d/%m/%Y")
                }
            )
        else:
            print("Ping unsuccessful")
            cell_path_pcs["offline"].append(
                {
                    "asset_number": host,
                    "last_unsuccessful_ping": today.strftime("%d/%m/%Y")
                }
            )

        restart_loop = input("Enter another asset number? (Y/N):\n").lower()
        if restart_loop == "y" or restart_loop == "yes":
            continue
        else: 
            break


myping()
print(cell_path_pcs)