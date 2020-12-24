import re





def app():
 with open('Challange02_input', 'r') as f:
    mylist = [line.strip() for line in f]
    pattern = "[0-9]+-[0-9]+[\s]+[a-z]+:[\s]+[a-z]+[a-z]"
    minim = "\d{1,2}"
    maxim = "-\d{1,2}"
    string = "[a-z]+[a-z]"
    litera = "[a-z]"
    k = 0

    pos = 0

    ki = 0
    kj = 0

    count = 0



 for o in mylist:

    x = re.search(pattern, str(o))
    mini = re.search(minim, str(o))
    maxi = re.search(maxim, str(o))
    strin = re.search(string, str(o))
    liter = re.search(litera, str(o))

    if (x):
        minimul = mini.group()
        maximul = maxi.group().strip("-")
        stringul = strin.group()
        literaa = liter.group()

        pos_a = minimul
        pos_b = maximul

        #pos_a= int(pos_aa) -1
        #pos_b=int(pos_bb) -1



        print("\npos a: " + str(pos_a) + "\npos b: " + str( pos_b) + "\npass: " + stringul + " \nletter: " + literaa)

    ki = 0
    kj = 0
    for (pos_i,i) in enumerate(stringul,start=1):
            print('pos_i : {}  i: {}'.format(pos_i,i))

            if(i == str(literaa)):

                if(pos_i == int(pos_a)):
                    ki=1

                elif(pos_i == int(pos_b)):
                   kj=1





    print('ki : {}    kj: {}'.format(ki, kj))
    if ((ki == 1) and (kj == 1)):
        print(" INVALID, both the same")
    elif ((ki == 0) and (kj == 0)):
        print("not in string")
    elif ((ki == 0) and (kj == 1)):
        print("VALID, they different")
        count += 1
    elif ((kj == 0) and (ki == 1)):
        print("VALID, they different")
        count += 1

    print('answer: {}'.format(count))


app()