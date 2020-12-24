with open('Challange01_Input', 'r') as f:
    mylist = [line.strip() for line in f]

    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            for k in range(j+1,len(mylist)):
             if(int(mylist[i])+int(mylist[j])+int(mylist[k])==2020):

               answer = int(mylist[i])*int(mylist[j]) * int(mylist[k])
               print('first number: '+mylist[i]+'\n'+'second number: ' +mylist[j]+'\n' + 'third number: ' + mylist[k] +'\n')
               print('answer : '+ str(answer))


