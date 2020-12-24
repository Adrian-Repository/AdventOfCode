import re

with open('Challange02_input', 'r') as f:
    mylist = [line.strip() for line in f]
    pattern = "[0-9]+-[0-9]+[\s]+[a-z]+:[\s]+[a-z]+[a-z]"
    minim = "\d{1,2}"
    maxim = "-\d{1,2}"
    string = "[a-z]+[a-z]"
    litera = "[a-z]"
    k=0
    new_list= []
o=0
for i in mylist:

    x = re.search(pattern, str(i))
    mini = re.search(minim, str(i))
    maxi = re.search(maxim, str(i))
    strin = re.search(string, str(i))
    liter = re.search(litera,str(i))

    if (x):

        minimul =  mini.group()
        maximul =  maxi.group().strip("-")
        stringul = strin.group()
        literaa = liter.group()
        
        print("minimul  : "+str(minimul) + " maximul  : " + str(maximul) + " pass: " + stringul + "  litera: " + liter.group())


    for j in stringul:

        if (j == (str(literaa))):
            k+=1

            if (k >= (int(minimul)) and (k <= int(maximul))):

                print(str(minimul)+" <= " + str(k) + " <= " + str(maximul))



    if (k >= (int(minimul)) and (k <= int(maximul))):
        o += 1
    k=0


print(o)

