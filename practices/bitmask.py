def check_bit4(number):
    mask = 0b1000
    desired = number & mask
    print bin(desired)
    if bin(desired) == 0b1000:
        return "on"
    else:
        return "off"
        
print check_bit4(0b1010)