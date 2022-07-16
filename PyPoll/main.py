import os
import csv

PyPoll_csv = os.path.join(".", "Resources","election_data.csv")

#Setting empty lists to store data from Data set
ballot = []
listofcandidates = []
uniquecandidates_list = []

#Opening and Reading PyPoll csv
with open(PyPoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    #Storing HeaderRow
    header_row = next(csv_file)


    for row in csv_reader:
        #Storing ballots and candidates into lists
        ballot.append(row[0])
        listofcandidates.append(row[2])


#Calculating Total Votes casted using len function 
TotalVotes = len(ballot)

#Extracting and storing a complete list of candidates who recieved votes
for c in listofcandidates:
    if c not in uniquecandidates_list:
        uniquecandidates_list.append(c)


#Counting number of Votes per candidate
VotesForCandidate1 = listofcandidates.count(uniquecandidates_list[0])
VotesForCandidate2 = listofcandidates.count(uniquecandidates_list[1])
VotesForCandidate3 = listofcandidates.count(uniquecandidates_list[2])

#Calculating vote percentage per candidate
PercentageC1 = round((int(VotesForCandidate1)/int(TotalVotes))*100,3)
PercentageC2 = round((int(VotesForCandidate2)/int(TotalVotes))*100,3)
PercentageC3 = round((int(VotesForCandidate3)/int(TotalVotes))*100,3)

#Adding Candidate name and corresponding number of votes in dictionary to get the winner
CandidatesDictionary = {uniquecandidates_list[0]:int(VotesForCandidate1), uniquecandidates_list[1]:int(VotesForCandidate2), uniquecandidates_list[2]:int(VotesForCandidate3)}

winner = max(CandidatesDictionary, key=CandidatesDictionary.get)


#Formatting and storing the desired result in a Variable called "result_PyPoll"
result_PyPoll = f"""
Election Results
--------------------------
Total Votes: {TotalVotes}       
--------------------------
{uniquecandidates_list[0]} : {PercentageC1}% ({VotesForCandidate1})
{uniquecandidates_list[1]} : {PercentageC2}% ({VotesForCandidate2})
{uniquecandidates_list[2]} : {PercentageC3}% ({VotesForCandidate3})
--------------------------
Winner: {winner}
--------------------------
"""
#Printing Result
print(result_PyPoll)


#Exporting result to a Txt.file in the analysis folder
output_path = os.path.join("analysis", "result_PyPoll.txt")
with open (output_path, 'w') as textfile:
    textfile.write(result_PyPoll)






    





    








