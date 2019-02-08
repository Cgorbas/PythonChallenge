#Pybank challenge
#
# importing os and csv dictionaries
#
import os
import csv
# initializing variables
numMonths = 0
profLossTotal = 0
n = 0
numRows = 0
maxAmt = 0
minAmt = 0
avgProfLoss = 0
maxMon = ""
minMon = ""
nameDate = ""

#Reading file
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(pybank_csv, newline="") as csvfile:

    pybankreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    for row in pybankreader:
        #        maxAmt = row[1]
        #        minAmt= row[1]
       #compensates for header",
        numRows = numRows+1

#sum,
        profLossTotal = profLossTotal + int(row[1])

#counts months\n",
        if nameDate != row[0]:
            nameDate = row[0]
            numMonths = numMonths + 1
        else:
            numMonths = numMonths

#finds Maximum change in profit    \n",
        if maxAmt < int(row[1]):
            maxAmt = int(row[1])
            maxMon = row[0]
        else:
            maxAmt = maxAmt

#finds Minimum
        if minAmt > int(row[1]):
            minAmt = int(row[1])
            minMon = row[0]
        else:
            minAmt = minAmt

#testing code
        print(str(numRows))
        print(row[0])
        print(str(profLossTotal))
#    minAmt=min(1  for row in csv.reader)
    avgProfLoss = profLossTotal/numRows
    print("this is the max amount: " + str(maxAmt))
    print("this is the min amount: " + str(minAmt))
    print("this is the average:  " + str(int(profLossTotal/numRows)))