while True:
    l = list(input().split(":"))
    d = {
        1:"",
        2:"",
        3:"",
        4:"",
        5:"",
        6:"",
        7:""
    }
    if l != ['end']:
        for x in range(2):
            for y in range(2):
                if l[x][y] == "0":
                    d[1]+= "+---+"
                    d[2]+= "|   |"
                    d[3]+= "|   |"
                    d[4]+= "+   +"
                    d[5]+= "|   |"
                    d[6]+= "|   |"
                    d[7]+= "+---+"
                elif l[x][y] == "1":
                    d[1]+= "    +"
                    d[2]+= "    |"
                    d[3]+= "    |"
                    d[4]+= "    +"
                    d[5]+= "    |"
                    d[6]+= "    |"
                    d[7]+= "    +"
                elif l[x][y] == "2":
                    d[1]+= "+---+"
                    d[2]+= "    |"
                    d[3]+= "    |"
                    d[4]+= "+---+"
                    d[5]+= "|    "
                    d[6]+= "|    "
                    d[7]+= "+---+"
                elif l[x][y] == "3":
                    d[1]+= "+---+"
                    d[2]+= "    |"
                    d[3]+= "    |"
                    d[4]+= "+---+"
                    d[5]+= "    |"
                    d[6]+= "    |"
                    d[7]+= "+---+"
                elif l[x][y] == "4":
                    d[1]+= "+   +"
                    d[2]+= "|   |"
                    d[3]+= "|   |"
                    d[4]+= "+---+"
                    d[5]+= "    |"
                    d[6]+= "    |"
                    d[7]+= "    +"
                elif l[x][y] == "5":
                    d[1]+= "+---+"
                    d[2]+= "|    "
                    d[3]+= "|    "
                    d[4]+= "+---+"
                    d[5]+= "    |"
                    d[6]+= "    |"
                    d[7]+= "+---+"
                elif l[x][y] == "6":
                    d[1]+= "+---+"
                    d[2]+= "|    "
                    d[3]+= "|    "
                    d[4]+= "+---+"
                    d[5]+= "|   |"
                    d[6]+= "|   |"
                    d[7]+= "+---+"
                elif l[x][y] == "7":
                    d[1]+= "+---+"
                    d[2]+= "    |"
                    d[3]+= "    |"
                    d[4]+= "    +"
                    d[5]+= "    |"
                    d[6]+= "    |"
                    d[7]+= "    +"
                elif l[x][y] == "8":
                    d[1]+= "+---+"
                    d[2]+= "|   |"
                    d[3]+= "|   |"
                    d[4]+= "+---+"
                    d[5]+= "|   |"
                    d[6]+= "|   |"
                    d[7]+= "+---+"
                else:
                    d[1]+= "+---+"
                    d[2]+= "|   |"
                    d[3]+= "|   |"
                    d[4]+= "+---+"
                    d[5]+= "    |"
                    d[6]+= "    |"
                    d[7]+= "+---+"
                if y != 1:
                    d[1]+= "  "
                    d[2]+= "  "
                    d[3]+= "  "
                    d[4]+= "  "
                    d[5]+= "  "
                    d[6]+= "  "
                    d[7]+= "  "

            if x == 0:
                d[1]+= "     "
                d[2]+= "     "
                d[3]+= "  o  "
                d[4]+= "     "
                d[5]+= "  o  "
                d[6]+= "     "
                d[7]+= "     "
    else:
        print("end")
        break
    for i in range(1, 8):
        print(d[i])
    print()
    print()
