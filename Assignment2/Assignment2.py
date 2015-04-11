__author__ = 'indrajeet'
import csv
g_dataDict = {}
g_term = []
g_doc = {}
g_numUser = 2
g_numTerms = 10
g_numDocs = 20
g_users = []
g_userRating = {}
def readXls(DEBUG=False):
    with open("Assignment2.csv","r") as fh:
        reader=csv.reader(fh)
        count=0
        tcount=0
        for line in reader:
            if count == 0:
                for x in line:
                    if(x != '' and tcount != g_numTerms):
                        #g_term.setdefault(tcount,x)
                        g_term.append(x)
                        tcount+=1
                    elif(x == 'num-attr' or x == ''):
                        pass
                    else:
                        g_users.append(x)
                        g_userRating.setdefault(x,{})

                # if(DEBUG):
                #     print(g_term)
                #     print(g_userRating)
                count+=1
            else:
                if(line[0] == 'DF'):
                    pass
                else:
                    g_doc.setdefault(line[0],{})
                    for x in range(1,len(line)-3):
                        g_doc[line[0]][x]=int(line[x])
                    for x in range(g_numUser):
                        tindex = len(line)-2+x
                        if(line[tindex] != ''):
                            g_userRating[g_users[x]][line[0]]=int(line[tindex])
                        else:
                            g_userRating[g_users[x]][line[0]]=int(0)
                    #if(DEBUG):
                        #print(g_doc)
                        #print(len(g_userRating[g_users[0]]))

readXls(DEBUG=False)