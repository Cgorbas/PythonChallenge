{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Pybank challenge\n",
    "#\n",
    "# importing os and csv dictionaries\n",
    "#\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [],
   "source": [
    "# initializing variables\n",
    "numMonths = 0\n",
    "profLossTotal = 0\n",
    "numMonths= 0\n",
    "nameDate =\"\"\n",
    "numRows=0\n",
    "maxAmt=0\n",
    "minAmt=0\n",
    "maxMon=\"\"\n",
    "minMon=\"\"\n",
    "avgProfLoss=0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Header: Date,Profit/Losses\n",
      "\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#Reading file\n",
    "pybank_csv = os.path.join(\"..\", \"Resources\", \"budget_data.csv\")\n",
    "\n",
    "# Open and read csv\n",
    "with open(pybank_csv, newline=\"\") as csvfile:\n",
    "\n",
    "    pybankreader = csv.reader(csvfile, delimiter=\",\")\n",
    "\n",
    "# Read the header row first (skip this part if there is no header)\n",
    "    csv_header = next(csvfile)\n",
    "    print(f\"Header: {csv_header}\")\n",
    "    for row in pybankreader:\n",
    "    \n",
    "#compensates for header\n",
    "        numRows= numRows+1\n",
    "\n",
    "#sum\n",
    "        profLossTotal = profLossTotal + int(row[1])\n",
    "        \n",
    "#counts months\n",
    "        if nameDate != row[0]:\n",
    "            nameDate=row[0]\n",
    "            numMonths = numMonths + 1\n",
    "        else:\n",
    "            numMonths=numMonths\n",
    "#finds Maximum change in profit    \n",
    "        if maxAmt < int(row[1]):\n",
    "            maxAmt = int(row[1])\n",
    "            maxMon = row[0]\n",
    "        else:\n",
    "            maxAmt= maxAmt\n",
    "\n",
    "#finds minimum \n",
    "        if minAmt > int(row[1]):\n",
    "            minAmt = int(row[1])\n",
    "            minMon = row[0]\n",
    "        else:\n",
    "            minAmt= minAmt\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Financial Analysis\n",
      "--------------------------------------\n",
      "Total Months:                       86\n",
      "Total:                              $38382578\n",
      "Average Change:                     $446309\n",
      "Greatest increase in profits:  Feb  ($1170593)\n",
      "Greatest decrease in profits:  Sep  ($-1196225)\n"
     ]
    }
   ],
   "source": [
    "#\n",
    "print(\"      Financial Analysis\"  )\n",
    "print(\"--------------------------------------\")\n",
    "print(\"Total Months:                       \"+ str(numMonths) )\n",
    "print(\"Total:                              $\" + str(profLossTotal) )\n",
    "print(\"Average Change:                     $\" +  str(int(profLossTotal/numRows)) )\n",
    "print(\"Greatest increase in profits:  \"  + maxMon[0:3] + \"  ($\" + str(maxAmt) + \")\" )\n",
    "print(\"Greatest decrease in profits:  \" + minMon[0:3]  + \"  ($\"+ str(minAmt) + \")\" )\n",
    "#print(\"Greatest increase in profits:  \" + maxMon[0:3]  +\"($\"+ str(maxAmt)\")\" )\n",
    "#print(\"Greatest decrease in profits:  \" + maxMon[0:3]  +\"($\"+str(minAmt)\")\" )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [],
   "source": [
    "#export a text file with the results\n",
    "#e(\"Maybe someday, he will promote me to a real file.\\n\")\n",
    "PyBank_data = open(\"PyBank_data.txt\",\"w\") \n",
    "PyBank_data.write(\"      Financial Analysis  \\n\")\n",
    "PyBank_data.write(\"--------------------------------------\\n\")\n",
    "PyBank_data.write(\"Total Months:                       \"+ str(numMonths) +\"\\n\")\n",
    "PyBank_data.write(\"Total:                              $\" + str(profLossTotal)+\"\\n\" )\n",
    "PyBank_data.write(\"Average Change:                     $\" +  str(int(profLossTotal/numRows))+\"\\n\" )\n",
    "PyBank_data.write(\"Greatest increase in profits:  \"  + maxMon[0:3] + \"  ($\" + str(maxAmt) + \")\\n\" )\n",
    "PyBank_data.write(\"Greatest decrease in profits:  \" + minMon[0:3]  + \"  ($\"+ str(minAmt) + \")\\n\" )\n",
    "PyBank_data.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
