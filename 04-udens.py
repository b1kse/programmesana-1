udens = True
while udens:
    temperatura = int(input("Kāda ir ūdens temperatūra?"))
    if -273 < temperatura <= 0:
        print("Ūdens ir ciets")
    elif 0< temperatura <100:
        print("Ūdens ir šķidrs")
    elif udens <= -273:
        print("beidzu")
        udens = False
    else:
        print("Ūdens ir gāze")
