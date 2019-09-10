def multiple_table():
    one=1
    while one<=9:
        two=1
        while two<=one:
            print("%d * %d = %d" %(one,two,one*two),end="\t")
            two+=1
        print("")
        one+=1