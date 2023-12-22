Weight = input("Hello Enter your Weight: ")
print(Weight)
KorP = input("Convert to (k)g or (l)bs?) ")
print(KorP)

if KorP.upper() == "L":
    print(float(Weight)*2.20462, "pounds")
else:
    print(float(Weight)*0.453592, "kg")

