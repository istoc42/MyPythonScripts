"""
Script that formats customer names.
"""

def format_customer(firstname, lastname, location=''):
    if location:
        customer = str(firstname) + ' ' + str(lastname) + ' ' + '(' + str(location) + ')'
        return customer
    else:
        customer = str(firstname) + ' ' + str(lastname)
        return customer
    
print(format_customer('John', 'Smith', location='California'))
