y="2020"
m="09"
d="22"
th="13"
tm="05"


def main():
    isoFile = open("C:\\Users\\slelenia\\Desktop\\ISOTEST.txt","w")
    iso=y+"-"+m+"-"+d+" "+th+":"+tm
    print(iso,file=isoFile)
    isoFile.close()

main()
    
    


