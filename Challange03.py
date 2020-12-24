with open('Challange03_input.txt', 'r') as f:
    mylist = [line.strip() for line in f]


#for x in mylist:
    #print('\n' + str(x))


    for pos_i,i in enumerate(mylist):
        for pos_j,j in enumerate(mylist):
            if(i==2 and j==3):
             print('i = {} \n j = {}'.format(i,j))

