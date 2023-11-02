from datetime import datetime
tagad = datetime.now()
stunda = tagad.hour

pulkstens = int(input("Cik ir pulksten?"))
if pulkstens <= 6:
    print("Labrīt!")
elif pulkstens >12:
    print("Labdien!")
elif pulkstnes >18:
    print("Labvakar!")
else:
    print("Arlabunakti!")
