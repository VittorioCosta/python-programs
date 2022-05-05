from math import pi, sqrt

area_sfera_val = 0.0
volume_sfera_val = 0.0
area_cilindro_val = 0.0
volume_cilindro_val = 0.0
area_cono_val = 0.0
volume_cono_val = 0.0

##noti r e h calcola area e volume di: sfera, cilindro, cono in una tabella
#param altezza e volume 
#return area e volume di: sfera, cilindro, cono
#
def main():
    #input
    h = float(input("h---> "))
    r = float(input("r---> "))
    #chiamo funzioni
    area_sfera(r)
    volume_sfera(r)
    area_cilindro(h,r)
    volume_cilindro(h,r)
    area_cono(h,r)
    volume_cono(h,r)
    print("area sfera %2.1f"% area_sfera_val)
    print("volume sfera %2.1f"% volume_sfera_val)
    print("area cilindro %2.1f"% area_cilindro_val)
    print("volume cilindro %2.1f"% volume_cilindro_val)
    print("area cono %2.1f"% area_cono_val)
    print("volume cono %2.1f"% volume_cono_val)


def area_sfera(r):
    global area_sfera_val
    area = 4*pi*(r**3)
    area_sfera_val = round(area, 1)
    return

def volume_sfera(r):
    global volume_sfera_val
    volume = (4/3)*pi*(r**3)
    volume_sfera_val = round(volume, 1)
    return

def area_cilindro(h,r):
    global area_cilindro_val
    area = 2*pi*r*(h+r)
    area_cilindro_val = round(area, 1)
    return

def volume_cilindro(h,r):
    global volume_cilindro_val
    volume = pi*h*r**2
    volume_cilindro_val = round(volume, 1)
    return

def area_cono(h,r):
    global area_cono_val
    area = pi*r*sqrt(r**2 + h**2)
    area_cono_val = round(area, 1)
    return

def volume_cono(h,r):
    global volume_cono_val
    volume = (pi*(r**2)*h)/3
    volume_cono_val = round(volume, 1)
    return
     
main()
    

