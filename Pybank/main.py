import os
import csv
from typing import Text

pybankpath = os.path.join('Resources','budget_data.csv')
month_count=0
totalpl = 0
total_change = 0
previous = 0
greatest_inc = 0
greatest_dec = 0
with open(pybankpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #next(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        #print(row)
        month_count = month_count + 1
        totalpl = totalpl + int(row[1])
        if previous != 0:
            change = int(row[1]) - int(previous)
            total_change = int(total_change) + int(change)
        previous = row[1]
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_increase = f"Greatest increase in profit: {row[0]} (${row[1]})"
        elif int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_decrease = f"Greatest Decrease in profit: {row[0]} (${row[1]})"

    average_change = int(total_change)/int(month_count)

    print(f"Total Months: {month_count}")
    print(f"Total: ${totalpl}")
    print(f"Average Change: ${round(average_change,2)}")
    print(greatest_increase)
    print(greatest_decrease)

analysis_printout = os.path.join('analysis','anayltsis.txt')    

print(analysis_printout)
with open(analysis_printout,'w') as txtfile:
    
    txtfile.write(f"Total Months: {month_count}\n")
    txtfile.write(f"Total: ${totalpl}\n")
    txtfile.write(f"Average Change: ${round(average_change,2)}\n")
    txtfile.write(f"{greatest_increase}\n")
    txtfile.write(f"{greatest_decrease}\n")