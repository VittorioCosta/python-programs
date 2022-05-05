a = str(input("floz, gal, oz,ft "))
b = str(input("ml,l,g,kg, cm, m "))

insL = ("floz","gal","ml","l")
insG = ("oz", "g","kg")
insM = ("ft", "mi", "cm", "m")



if a in insL and b in insL: pass
elif a in insG and b in insG: pass
elif a in insM and b in insM: pass
else: print("le misure non sono compatibili"), exit()

c = float(input("valore "))

floz_ml = c*30
floz_l = c*0.03
gal_ml = c*4546
gal_lt = c*4,54609
oz_g = c*28.5
oz_kg = c*0.0285
ft_m = c*0.3048
ft_cm = c*30.48



if a in insL and b in insL:
    if a=="floz" and b=="ml": print(floz_ml, b)
    elif a=="floz" and b=="l": print(floz_l, b)
    elif a=="gal" and b=="ml":print(gal_ml, b)
    elif a=="gal" and b=="l": print(gal_l, b)
elif a in insG and b in insG:
    if a=="oz" and b=="g": print(oz_g, b)
    if a=="oz" and b=="kg": print(oz_kg, b)
elif a in insM and b in insM:
    if a=="ft" and b=="m": print(ft_m, b)
    if a=="ft" and b=="cm": print(ft_cm, b)





