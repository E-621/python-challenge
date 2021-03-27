#Import modules
import os
import csv

#set path for csv file
csvpath = os.path.join('Resources','election_data.csv')

#set variables
totalvotes = 0
Khan=0
Correy=0
Li=0
otooley = 0

#open csv file
with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #begin loop statement   
    for row in csvreader:
      totalvotes += 1
      if row[2].strip()=="Khan":
        Khan+=1
      elif row[2].strip()=="Correy":
        Correy+=1
      elif row[2].strip()=="Li":
        Li +=1
      else: 
        otooley += 1

 #show output       
print("Election Results")
print("-------------------------")

print(f"Total Votes: {totalvotes}")
print("-------------------------")
khanpercent = "{:.3f}".format(Khan/totalvotes*100)
correypercent = "{:.3f}".format(Correy/totalvotes*100)
lipercent = "{:.3f}".format(Li/totalvotes*100)
otooleypercent = "{:.3f}".format(otooley/totalvotes*100)
print(f"Khan: {khanpercent}% ({Khan})")
print(f"Correy: {correypercent}% ({Correy})")
print(f"Li: {lipercent}% ({Li})")
print(f"otooley: {otooleypercent}% ({otooley})")
print("-------------------------")
canidates = {}
canidates["Khan"]=Khan
canidates["Correy"]=Correy
canidates["Li"]=Li
canidates["otooley"]=otooley
print(f"Winner: {max(canidates,key=canidates.get)}")
print("-------------------------")

#output to csv
with open("Poll Results.txt","w") as asfile:
  asfile.write("Election Results\n")
  asfile.write("-------------------------\n")
  asfile.write(f"Total Votes: {totalvotes}\n")
  asfile.write("-------------------------\n")
  asfile.write(f"Khan: {khanpercent}% ({Khan})\n")
  asfile.write(f"Correy: {correypercent}% ({Correy})\n")
  asfile.write(f"Li: {lipercent}% ({Li})\n")
  asfile.write(f"otooley: {otooleypercent}% ({otooley})\n")
  asfile.write("-------------------------\n")
  asfile.write(f"Winner: {max(canidates,key=canidates.get)}\n")
  asfile.write("-------------------------\n")