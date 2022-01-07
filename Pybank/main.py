# import required libraries for code
import os
import csv
from typing import Text
# create path to the budget_data csv file to start analysing data
pybankpath = os.path.join('Resources','budget_data.csv')
# create variables and setting values to 0 allowing for calculations
month_count=0
totalpl = 0
total_change = 0
previous = 0
greatest_inc = 0
greatest_dec = 0
# open csvfile to pull data
with open(pybankpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        # counting the months for total months
        month_count = month_count + 1
        # calculating the total profit/loss
        totalpl = totalpl + int(row[1])
        # calculating the total change
        if previous != 0:
            change = int(row[1]) - int(previous)
            total_change = int(total_change) + int(change)
        previous = row[1]
        # storing the value of the greatest increase/decrease
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_increase = f"Greatest increase in profit: {row[0]} (${row[1]})"
        elif int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_decrease = f"Greatest Decrease in profit: {row[0]} (${row[1]})"
    # calculate average change in profit/lose
    average_change = int(total_change)/int(month_count)
    #print all values obtained in requested format 
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${totalpl}")
    print(f"Average Change: ${round(average_change,2)}")
    print(greatest_increase)
    print(greatest_decrease)
# create path to analysis folder to create analysis text file
analysis_printout = os.path.join('analysis','anaylsis.txt')   
# open the analysis file and write/save my output to the file
with open(analysis_printout,'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {month_count}\n")
    txtfile.write(f"Total: ${totalpl}\n")
    txtfile.write(f"Average Change: ${round(average_change,2)}\n")
    txtfile.write(f"{greatest_increase}\n")
    txtfile.write(f"{greatest_decrease}\n")