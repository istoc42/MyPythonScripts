# with open("read_and_write\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("read_and_write\my_file.txt", mode="a") as file:
    file.write("\nThis is new text.")