import os
import csv

csvpath = os.path.join("resources",'budget_data.csv')
totalmonths = 1
profitloss = 0
previousProfitLoss = 0
netProfitLoss = 0
netChangeList =[]
total = 0
months =[]
with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    firstrow = next(csvreader)
    profitloss = int(firstrow[1])
    previousProfitLoss = profitloss
    
    for row in csvreader:
        total += int(row[1])
        months.append(row[0])
        totalmonths = totalmonths + 1
        profitloss = int(row[1])
        netProfitLoss = profitloss - previousProfitLoss
        previousProfitLoss = profitloss
        netChangeList += [netProfitLoss]
        #print(netProfitLoss)
print("Financial Analysis")
print("-------------------------")
average = sum(netChangeList)/len(netChangeList)
print(sum(netChangeList))
print(f"Total Months: {totalmonths}")
print(f"Total: ${total}")

print(f"Average Change: ${round(average,2)}")
maxprofit=netChangeList.index(max(netChangeList))
minimumprofit=netChangeList.index(min(netChangeList))
print(f"Greatest Increase in Profits: {months[maxprofit]} (${max(netChangeList)})")
print(f"Greatest Decrease in Profit: {months[minimumprofit]} (${min(netChangeList)})")