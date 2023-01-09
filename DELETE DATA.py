"""
This program is to delete the data collected by the reaction test.
This will fully wipe the leaderboards and data cannot be recovered.

-Noha Epiney
"""

import pickle

with open("test.pickle","rb") as infile:
    resultlist = pickle.load(infile)

print(resultlist)

selection = int(input("Confirmation of data supression (yes): "))


if selection == yes:
    resultlist = ["time","name","age"]

    with open("test.pickle","wb") as outfile:
        pickle.dump(resultlist,outfile)

    print("Data supression complete")
