n = -1
b = False

def main():
    string=str(input("Parola---> "))
    match=str(input("Stringa---> "))
    print("\n")
    return print(find(string, match))

def find(s,m):
    global n
    global b
    match=""
    match=s[n:]
    n -= 1
    if match == m:
        print("fuck")
        b = True
        return b      
    if match != m and len(s) != len(match):
        find(s,m)
    return b
 
main()
    
