import sys

pin = 1234

input_ = int(input("PIN"))

if input_ == pin: print("Benvenuto")

input_ = int(input("secondo tentativo... PIN "))

if input_ == pin: print("Benvenuto")

input_ = int(input("terzo tentativo... PIN "))


if input_ == pin: print("benvenuto")
elif input_ != pin: print('''CARTA BLOCCATA,
RIVOLGERSI AL PROPRIO ISTITUTO'''), sys.exit()


