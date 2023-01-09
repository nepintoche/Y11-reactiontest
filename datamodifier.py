"""
Running this program will change all results recorded in seconds in the reaction test
and convert them to miliseconds

-Noha Epiney

"""
import pickle

with open("test.pickle","rb") as infile:
        resultlist = pickle.load(infile)

print(resultlist)

for count,i in enumerate(resultlist):
        if type(resultlist[count][0]) == float:
                resultlist[count][0] = int((round(resultlist[count][0],3))*1000)


print(resultlist)

with open("test.pickle","wb") as outfile:
        pickle.dump(resultlist,outfile)
