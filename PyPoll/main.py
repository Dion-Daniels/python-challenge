#Import libraries
import csv
import os
# Create path to dataset/csv file
pollpath = os.path.join('Resources','election_data.csv')
# Create variables
totalvotes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
#open dataset to begin reading data
with open(pollpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        # Tally total votes
        totalvotes = totalvotes + 1
        # Determine which candidate got the vote and tally vote towards them
        if row[2] == 'Khan':
            khan_votes = khan_votes + 1
        elif row[2] == 'Correy':
            correy_votes = correy_votes + 1
        elif row[2] == 'Li':
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

# create function to condense code and calculate percentages
def percentage(candidate_votes, total_votes):
  percentage = 100 * float(candidate_votes)/float(total_votes)
  percentage = "%.3f" % round(percentage,3)
  return str(percentage) + "%"
# Calculate percentages
Khan = (percentage(khan_votes,totalvotes))
Correy = (percentage(correy_votes,totalvotes))
Li = (percentage(li_votes,totalvotes))
OTooley = (percentage(otooley_votes,totalvotes))
# Determine the winner of the election
if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
    winner = "Khan"
if correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
    winner = "Correy"
if li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes:
    winner = "Li"
if otooley_votes > khan_votes and otooley_votes > correy_votes and otooley_votes > li_votes:
    winner = "O'Tooley"
# print out results to the election
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
print(f"Khan: {Khan} ({khan_votes})")
print(f"Correy: {Correy} ({correy_votes})")
print(f"Li:{Li} ({li_votes})")
print(f"O'Tooley: {OTooley} ({otooley_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# create path to analysis folder to create analysis text file
analysis_printout = os.path.join('analysis','anaylsis.txt')   
# open the analysis file and write/save my output to the file
with open(analysis_printout,'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalvotes}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Khan: {Khan} ({khan_votes})\n")
    txtfile.write(f"Correy: {Correy} ({correy_votes})\n")
    txtfile.write(f"Li:{Li} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {OTooley} ({otooley_votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")