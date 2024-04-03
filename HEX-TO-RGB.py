# AUTHOR:- KUSH SHAH
def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    print(hex)
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

hex = input("Enter hex color: ")
print("RGB: %s" % str(hex_to_rgb(hex)))