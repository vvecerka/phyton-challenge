import os
import csv
budget_data = os.path.join("Resources","budget_data.csv")

#lists to store data
total_months=[]
net_total=[]
change=[]
average_change=[]
greatest_increase = []
greatest_decrease =[]
with open(budget_data.csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        total_months.append(row[0])
        net_total=sum(row[1])
        average_change
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']})")
