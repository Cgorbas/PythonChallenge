{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
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
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initializing Variables\n",
    "votesCastTotal = 0\n",
    "ctRows = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Header: Voter ID,County,Candidate\n",
      "\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'set' object has no attribute 'get'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-28-b951cc5b3da1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     16\u001b[0m         \u001b[0mpypoll_data\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[0mrow\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mrow\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mrow\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[1;31m#remove after testing\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 18\u001b[1;33m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"column 1: \"\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mpypoll_data\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     19\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"column 2: \"\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpypoll_data\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"column 3: \"\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mpypoll_data\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'set' object has no attribute 'get'"
     ]
    }
   ],
   "source": [
    "#set of poll data called election_data.csv.  the dataset is composed of 3 columns:  Voter ID0,County1,Candidate2.\n",
    "#selects file in Resources folder\n",
    "#pypoll_csv = os.path.join(\"..\", \"Resources\", \"election_data.csv\")\n",
    "pypoll_csv = os.path.join(\"..\", \"Resources\", \"test_election_data.csv\")\n",
    "pypoll_data = {}\n",
    "# Open and read csv\n",
    "with open(pypoll_csv, newline=\"\") as csvfile:\n",
    "\n",
    "    pypollreader = csv.reader(csvfile, delimiter=\",\")\n",
    "\n",
    "# Read the header row first\n",
    "    csv_header = next(csvfile)\n",
    "    print(f\"Header: {csv_header}\")\n",
    "    for row in pypollreader: \n",
    "        ctRows= ctRows+1\n",
    "        pypoll_data = {row[2],row[0],row[1] }\n",
    "#remove after testing\n",
    "        print(\"column 1: \" + pypoll_data.get(0) )\n",
    "        print(\"column 2: \" + str(pypoll_data.get(1)) )\n",
    "        print(\"column 3: \" + pypoll_data[2] )\n",
    "\n",
    "        print(\"ctRows: \" + str(ctRows) )\n",
    "        \n",
    "#The total number of votes cast\n",
    "        votesCastTotal = ctRows \n",
    "    print(\"total votes cast: \" + str(votesCastTotal) )\n",
    "#end of csv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#working with dictionary pypolldata  candidate id count - populate pypoll_data\n",
    "# sort by candidate [0]\n",
    "# for row in pypolldata\n",
    "#   if candidate 1=\n",
    "#           dictionary append candidate, candidate total\n",
    "\n",
    "# set of poll data called election_data.csv.  the dataset is composed of 3 columns:  Voter ID0,County1,Candidate2.\n",
    "\n",
    "#d={}\n",
    "#for row in reader:\n",
    "#    d[row[0]]=row[1:]\n",
    "#\n",
    "#possibly, go through the files.  compare names, when you get to a new name, place the new name somewhere, an index?\n",
    "#also have a place to count the votes and place them into a dictionary.  say, create dictionary polls{}\n",
    "# with column 0 being the candidate and column1 being a count.  append? or change the values for the keys.  \n",
    "# would want to know how many candidates, and their respective votes\n",
    "# need % each candidate won of the vote, and the maxnum of votes for candidates.  perhaps use a for in to print out the percentages\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "# \n",
    "\n",
    "# Open and read csv\n",
    "\n",
    "    \n",
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
    "\n",
    "    votesCastTotal = numRows  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#   -The total number of votes cast\n",
    "#   -complete list of candidates who received votes\n",
    "#   -percentage of votes each candidate won\n",
    "#   -total number of votes each candidate won\n",
    "#   -winner of the election based on popular vote\n",
    "#\n",
    "#   -------------------------\n",
    "#TGotal Votes:    3135123\n",
    "#   ---------------------------\n",
    "#   Kahn:   54%  (23143)\n",
    "#   Kahn2:   53%  (231431)\n",
    "#   Kahn3:   51%  (23143)\n",
    "#   ---------------------------\n",
    "#Winner:  Khan\n",
    "#   ---------------------------\n",
    "# for ines in pypoll_data{}\n",
    "#print candidate [0]  candidatevotes[2]/votesCastTotal candidatevotes[2]   \n",
    "\n",
    "\n",
    "print(\" ***  Election Results  ***\"  )\n",
    "print(\"--------------------------------------\")\n",
    "print(\"Total Votes Cast:                       \"+ str(votesCastTotal) )\n",
    "print(\"--------------------------------------\")\n",
    "#print(\"Total Months:                       \"+ str(numMonths) )\n",
    "print(\"Total:                              $\" + str(profLossTotal) )\n",
    "print(\"Average Change:                     $\" +  str(int(profLossTotal/numRows)) )\n",
    "print(\"Greatest increase in profits:  \"  + maxMon[0:3] + \"  ($\" + str(maxAmt) + \")\" )\n",
    "print(\"Greatest decrease in profits:  \" + minMon[0:3]  + \"  ($\"+ str(minAmt) + \")\" )\n",
    "#print(\"Greatest increase in profits:  \" + maxMon[0:3]  +\"($\"+ str(maxAmt)\")\" )\n",
    "#print(\"Greatest decrease in profits:  \" + maxMon[0:3]  +\"($\"+str(minAmt)\")\" )\n",
    "\n",
    "\n",
    "#\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#in addition, final script should print the analysis to teh terminal and export a text file with the results\n",
    "#Note:  had intended to create in Resources folder but so far could not get it to work\n",
    "\n",
    "PyPoll_data = open(\"PyPoll_data.txt\",\"w\") \n",
    "PyPoll_data.write(\" ***  Election Results  ***\\n\")\n",
    "PyPoll_data.write(\"--------------------------------------\\n\")\n",
    "PyPoll_data.write(\"Total Votes Cast:                       \"+ str(votesCastTotal) +\"\\n\")\n",
    "PyPoll_data.write(\"--------------------------------------\\n\")\n",
    "#\n",
    "PyPoll_data.write(\"Total Months:                       \"+ str(numMonths) +\"\\n\")\n",
    "PyPoll_data.write(\"Total:                              $\" + str(profLossTotal)+\"\\n\" )\n",
    "PyPoll_data.write(\"Average Change:                     $\" +  str(int(profLossTotal/numRows))+\"\\n\" )\n",
    "PyPoll_data.write(\"Greatest increase in profits:  \"  + maxMon[0:3] + \"  ($\" + str(maxAmt) + \")\\n\" )\n",
    "PyPoll_data.write(\"Greatest decrease in profits:  \" + minMon[0:3]  + \"  ($\"+ str(minAmt) + \")\\n\" )\n",
    " \n",
    "PyPoll_data.close()"
   ]
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
