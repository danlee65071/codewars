def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    for i in pin:
        if i < '0' or i > '9':
            return False
    return True
