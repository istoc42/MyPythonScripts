from w10_master_list import cell_path_master_list as ml

def ping_all():
    for dictionary in ml:
        for val in dictionary.values():
            print('Hello')

# print(ml)