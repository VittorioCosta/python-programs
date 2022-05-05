s = float(input("spesa "))

if s>250: v = 0.14*s
elif s<=250 and s>150: v =0.12*s 
elif s<=150 and s>60: v =0.10*s
elif s<=60 and s>10: v =0.8*s
elif s<=10: print("you don't have win a coupon")

if s>250: t = "14%"
elif s<=250 and s>150: t = "12%" 
elif s<=150 and s>60: t = "10%"
elif s<=60 and s>10: t = "8%"

print("\nYou have win a coupon of %.2f £" % v)
print("("+t+" of your purchase)")

