#Import the CSV file
import os
import csv

#Locate the file path of the CSV file
election_data = os.path.join("resources/election_data.csv")


#Define variables
VoteList = []
Candidates = []
PerCentCandidate = []
CountOfCandidate = []

TotalVote = 0

#Open and read the file election_data.csv

with open(election_data, newline = "") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csvheader = next(csvreader)

#Read the row from using .append
	for row in csvreader:
        	VoteList.append(row[2])

TotalVote = len(VoteList)

#Find all candidates, assign the indexes
for Name in VoteList:
	if Name not in Candidates:
		Candidates.append(Name)
		x = Name

#Count for the total vote of each candidate
Count = 0

#Set the first candidate on the list to begin the loop
Candidate = VoteList[0]

LastCount = 0

for Candidate in Candidates:
	for Vote in VoteList:
		if Candidate == Vote:
			Count += 1
Percent = Count / len(VoteList)
PerCentCandidate.append(Percent)
CountOfCandidate.append(Count)

if LastCount < Count:
	Winner = Candidate
print(f"{Candidate}: {Percent:.3%} ({Count})")

#Reset the vote count to zero
LastCount = Count
Count = 0
#What information to display
print("Election Results")
print("------------------")
print(f"Total Votes: {TotalVote}")
print("---------------------")
print(f"Winner: {Winner}")
print("-------------------")

#Export into txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = ("-------------")
line3 = str(f"Total Votes: {str(TotalVote)}")
line4 = ("-------------")
line5 = str(f"Winner: {str(Winner)}")
output.write('{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5))