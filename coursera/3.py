def complementory_color(color):
    if color =="blue":
        complement = "orange"
    elif color =="yellow":
        complement = "purple"
    elif color=="red":
        complement = "green"
    else:
        complement = "unknown"
    return complement

print(complementory_color("blue"))