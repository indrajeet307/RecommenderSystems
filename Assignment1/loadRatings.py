from asyncore import read

__author__ = 'indrajeet'
import csv

g_movies=[]
g_users=[]
g_ratingsDict={} #movei ==> users
g_filpedRatings={}  #users ==> movies

def loadDict():
    with open("A1Ratings.csv","r") as fh:
        reader=csv.reader(fh)
        count=0
        for line in reader:
            if count==0:
                g_movies=line
                count+=1
                for x in range(1,len(line)):

                    g_ratingsDict.setdefault(line[x],{})
            else:
                g_users.append(line[0])
                for x in range(1,len(line)):
                    if line[x] != '':
                        g_ratingsDict[g_movies[x]][line[0]]=int(line[x])
                        #print (line[x])

def swap():
    for movie in g_ratingsDict:
        for user in g_ratingsDict[movie]:
            print(user),print(movie)
            g_filpedRatings.setdefault(user,{})
            g_filpedRatings[user][movie]=g_ratingsDict[movie][user]


def meanMovieRatings():
    loadDict()
    g_mean={}
    tot=0
    for movie in g_ratingsDict:
        for user in g_ratingsDict[movie]:
            tot+=g_ratingsDict[movie][user]

        tot=tot/float(len(g_ratingsDict[movie]))
        g_mean.setdefault(movie,{})
        g_mean[movie]=tot
        tot=0

    return g_mean

def rating4ormore():
    loadDict()
    g_rates={}
    tot=0
    for movie in g_ratingsDict:
        for user in g_ratingsDict[movie]:
            if g_ratingsDict[movie][user] >= 4:
                tot+=1
        tot=tot/float(len(g_ratingsDict[movie]))
        tot=tot*100
        g_rates.setdefault(movie,{})
        g_rates[movie]=tot
        tot=0

    return g_rates

def numofratings():
    loadDict()
    g_rates={}
    tot=0
    for movie in g_ratingsDict:
        tot=len(g_ratingsDict[movie])
        g_rates.setdefault(movie,{})
        g_rates[movie]=tot
        tot=0

    return g_rates

def starWars():
    loadDict()
    swap()
    g_rates={}
    sw1="260: Star Wars: Episode IV - A New Hope (1977)"
    tot=0
    tot2=len(g_ratingsDict[sw1])
    for movie in g_ratingsDict:
        for user in g_filpedRatings:
            if sw1 in g_filpedRatings[user] and movie in g_filpedRatings[user]:
                tot+=1
        tot=tot/float(tot2)
        g_rates.setdefault(movie,{})
        g_rates[movie]=tot
        tot=0

    return g_rates
import operator
def showAll():
    print("Que1")
    temp=meanMovieRatings()
    temp_x=sorted(temp.items(),key=operator.itemgetter(1))
    temp_x.reverse()
    for x in temp_x:
        print(x)

    print("Que2")
    temp=rating4ormore()
    temp_x=sorted(temp.items(),key=operator.itemgetter(1))
    temp_x.reverse()
    for x in temp_x:
        print(x)

    print("Que3")
    temp=numofratings()
    temp_x=sorted(temp.items(),key=operator.itemgetter(1))
    temp_x.reverse()
    for x in temp_x:
        print(x)

    print("Que4")
    temp=starWars()
    temp_x=sorted(temp.items(),key=operator.itemgetter(1))
    temp_x.reverse()
    for x in temp_x:
        print(x)

"""to run this code
 import operator
 temp=<funcName>
 temp_x=sorted(temp.items(),key=operator.itemgetter(1))
 print(temp_x)
 """
