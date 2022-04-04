#! python3

import os

sync_paige = f"aws s3 sync L:\\Cellular_Pathology\\Aperio_Images\\Paige_AI_Slides s3://056980e7-e102-f40e-d28f-18c9c062b2c1"

sync_aira = f"aws s3 sync L:\Cellular_Pathology\Histology\!PDL-1_India s3://aira-nhs-uk/images"

print("Choose which bucket to sync: ")
print("1. Paige AI")
print("2. Aira")

a = None
while a not in (1, 2):

    a = int(input())

    if a == 1:
        print("You have chosen Paige AI. Now sycning...")
        os.system(sync_paige)
        break
    if a == 2:
        print("You have chosen Aira. Now syncing...")
        os.system(sync_aira)
        break
    else:
        print("You have made an invalid choice, try again.")    
        print("Choose which bucket to sync: ")
        print("1. Paige AI")
        print("2. Aira")
