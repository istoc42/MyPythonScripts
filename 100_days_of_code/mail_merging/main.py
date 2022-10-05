#TODO: Create a letter using starting_letter.txt 
with open(r"mail_merging\Input\Names\invited_names.txt") as names:
    all_names = names.read().splitlines()

#for each name in invited_names.txt
with open(r"mail_merging\Input\Letters\starting_letter.txt", "r") as letter:
    letter_contents = letter.read()
    for name in all_names:
        # Replace the [name] placeholder with the actual name.
        new_letter = letter_contents.replace("[name]", name)
        # Save the letters in the folder "ReadyToSend".
        write_letter = open(f"mail_merging\\Output\\ReadyToSend\\letter_for_{name}.txt", "x")
        write_letter.write(new_letter)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp