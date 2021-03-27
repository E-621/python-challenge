#import modules
import os
import csv

#set path for csv file
csvpath = os.path.join('Resources','budget_data.csv')

#set variables
totalmonths = 1
profitloss = 0
previousProfitLoss = 0
netProfitLoss = 0
netChangeList =[]
total = 0
months =[]

#open csv file
with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    firstrow = next(csvreader)
    profitloss = int(firstrow[1])
    startdate = int(firstrow[1])
    previousProfitLoss = profitloss
    
    #begin loop statement
    for row in csvreader:
        total += int(row[1])
        months.append(row[0])
        totalmonths = totalmonths + 1
        profitloss = int(row[1])
        netProfitLoss = profitloss - previousProfitLoss
        previousProfitLoss = profitloss
        netChangeList += [netProfitLoss]
        #print(netProfitLoss)


#show output        
print("Financial Analysis")
print("-------------------------")
average = sum(netChangeList)/len(netChangeList)
#print(sum(netChangeList))
print(f"Total Months: {totalmonths}")
print(f"Total: ${total + startdate}")

print(f"Average Change: ${round(average,2)}")
maxprofit=netChangeList.index(max(netChangeList))
minimumprofit=netChangeList.index(min(netChangeList))
print(f"Greatest Increase in Profits: {months[maxprofit]} (${max(netChangeList)})")
print(f"Greatest Decrease in Profit: {months[minimumprofit]} (${min(netChangeList)})")

#output to csv
with open("PyBankAnalysis.txt","w") as asfile:
  asfile.write("Financial Analysis\n")
  asfile.write("-------------------------\n")
  asfile.write(f"Total Months: {totalmonths}\n")
  asfile.write(f"Total: ${total + startdate}\n")
  asfile.write(f"Average Change: ${round(average,2)}\n")
  asfile.write(f"Greatest Increase in Profits: {months[maxprofit]} (${max(netChangeList)})\n")
  asfile.write(f"Greatest Decrease in Profit: {months[minimumprofit]} (${min(netChangeList)})\n")