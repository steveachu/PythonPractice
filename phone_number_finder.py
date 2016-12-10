def isPhoneNumber(text):
    """This function will determine if a string is a phone number"""
    # Check length of the string
    if len(text) != 12:
        return False

    # Check three characters of the string to see if they are numbers
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    # Check if a hyphen is present
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

print('415-555-4242 is a phone number: ')
print(isPhoneNumber('415-555-4242'))
