#Import libraries
#Import libraries
import csv
import os
import collections
from collections import Counter
# Create path to dataset/csv file
pollpath = os.path.join('Resources','election_data.csv')
# Create variables
candidate_list = []
candidate_votes = []
percentage_vote = []
votes = Counter()
totalvotes = 0
winner = 0
# create function to condense code and calculate percentages
def percentage(candidate_votes, totalvotes):
  percentage = 100 * float(candidate_votes)/float(totalvotes)
  percentage = "%.3f" % round(percentage,3)
  return str(percentage) + "%"

#open dataset to begin reading data
with open(pollpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        # Tally total votes
        totalvotes = totalvotes + 1
        # Determine which candidate got the vote and tally vote towards them
        candidate_name = row [2]
        # add candidates into the candidate list
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
        # stores candidate name and votes counted
        votes[candidate_list[(candidate_list.index(candidate_name))]] += 1

for x in range(0,len(votes)):
    # update lists to make printout of results easier to read
    candidate_votes.append(votes[candidate_list[x]])
    percentage_vote.append(percentage(votes[candidate_list[x]],totalvotes))
    # Determine the winner of the election
    if (votes[candidate_list[x]]) > winner:
        winner = (votes[candidate_list[x]])
        winner_name = candidate_list[x]           

# print out results to the election
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
for x in range(0,len(votes)):
    print(f"{candidate_list[x]}: {percentage_vote[x]} ({candidate_votes[x]})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")
    

# create path to analysis folder to create analysis text file
analysis_printout = os.path.join('analysis','anaylsis.txt')   
# open the analysis file and write/save my output to the file
with open(analysis_printout,'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalvotes}\n")
    txtfile.write("-------------------------\n")
    for x in range(0,len(votes)):
        txtfile.write(f"{candidate_list[x]}: {percentage_vote[x]} ({candidate_votes[x]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write("-------------------------\n")    