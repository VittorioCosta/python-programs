while True:
    def main():
        year = int(input("year---> "))
        if year > 1582: return print(gregoriana(year))
        elif year <= 1582: return print(normal(year))
        
    def gregoriana(y):
        if y%400==0: return"bisestile"
        elif y%100==0: return "non bisestile"
        elif y%4==0: return "bisestile"
        else: return "solare"
    
    def normal(y):
        if y%4==0: return "bisestile"
        else: return "solare"
    
    main()
