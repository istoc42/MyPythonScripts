import platform
import subprocess
from w10_master_list import asset_list as al

successful = []

failed = []

def ping_all():
    for asset in al:
        parameter = '-n' if platform.system().lower()=='windows' else '-c'

        host = asset

        command = ['ping', parameter, '1', host]
        response = subprocess.call(command)

        

        if response == 0:
            print("Success")
            successful.append(
                {
                    "asset_num": host,
                }
            )
        else:
            print("Failed")
            failed.append(
                {
                    "asset_num": host,
                }
            )

ping_all()

print("Successful pings:")
print(successful)
print("\nFailed pings:")
print(failed)
