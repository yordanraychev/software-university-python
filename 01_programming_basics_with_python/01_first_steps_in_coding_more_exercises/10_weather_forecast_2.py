degrees = float(input())

if 26.0 <= degrees <= 35.0:
    print("Hot")
elif 20.1 <= degrees <= 25.9:
    print("Warm")
elif 15.0 <= degrees <= 20.0:
    print("Mild")
elif 12.0 <= degrees <= 14.9:
    print ("Cool")
elif 5.0 <= degrees <= 11.9:
    print ("Cold")
else:
    print("unknown")
